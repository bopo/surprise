# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django_filters import FilterSet, NumberFilter
from rest_framework import filters, viewsets, status
from rest_framework.response import Response
from rest_framework.reverse import reverse

from restful.helpers import ItemsGet
from restful.models.goods import Goods, GoodsCategory, QueryRule
from restful.serializers.goods import (
    GoodsCategorySerializer, GoodsSerializer,
    QuerySerializer)
from restful.views import BaseViewSet


class GoodsFilter(FilterSet):
    min_price = NumberFilter(name="price", lookup_type='gte')
    max_price = NumberFilter(name="price", lookup_type='lte')

    class Meta:
        model = Goods
        fields = ['category', 'min_price', 'max_price', 'recommend']
        search_fields = ('^name',)
        ordering_fields = '__all__'


class GoodsViewSet(viewsets.ReadOnlyModelViewSet, BaseViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = '__all__'

    search_fields = ('^name',)
    filter_fields = '__all__'

    filter_class = GoodsFilter

    # @action(methods=['post', 'get'], is_for_list=True, endpoint='comments')
    # def comments(self, request, pk=None):
    #     self.serializer_class = GoodsCommentSerializer
    #     self.filter_class = None
    #     self.filter_fields = None
    #
    #     if request.method == 'GET':
    #         self.queryset = self.get_object().goodscomment_set.all().order_by('-created')
    #         page = self.paginate_queryset(self.queryset)
    #         if page is not None:
    #             serializer = self.get_serializer(page, many=True, context={'request': request})
    #             return self.get_paginated_response(serializer.data)
    #     elif request.method == 'POST':
    #         self.permission_classes = (IsAuthenticated,)
    #         self.check_permissions(request)
    #
    #         serializer = self.get_serializer(data=request.data)
    #
    #         if serializer.is_valid():
    #             data = serializer.data
    #             data['goods'] = self.get_object()
    #             data['owner'] = request.user
    #             serializer.create(data)
    #             return Response({'status': 'comment set'}, status.HTTP_201_CREATED)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    获取商品分类数据

    子分类的调用方法 /api/v1.0/category/<父分类的ID>/children/ 返回的是该主分类的子分类的列表
    '''
    queryset = GoodsCategory.objects.filter(is_active=True)
    serializer_class = GoodsCategorySerializer
    # filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    # search_fields = ('=name',)
    # filter_fields = '__all__'
    # ordering_fields = '__all__'


# class GoodsCommentViewSet(viewsets.ModelViewSet):
#     queryset = GoodsComment.objects.all()
#     serializer_class = GoodsCommentSerializer
#     filter_fields = ('goods', 'owner')
#
#     def list(self, request, goods_pk=None):
#         queryset = GoodsComment.objects.filter(article=goods_pk)
#         serializer = GoodsCommentSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None, goods_pk=None):
#         queryset = GoodsComment.objects.filter(pk=pk, article=goods_pk)
#         maildrop = get_object_or_404(queryset, pk=pk)
#         serializer = GoodsCommentSerializer(maildrop)
#         return Response(serializer.data)
#
#     def create(self, request, goods_pk=None):
#         self.permission_classes = (IsAuthenticated,)
#         self.check_permissions(request)
#
#         request.data['owner'] = request.user.pk
#         request.data['goods'] = goods_pk
#
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
from rest_framework.viewsets import GenericViewSet
from django.core.cache import cache


class QueryViewSet(GenericViewSet):
    '''
    用来做上面的搜索接口 暂时只支持 `POST` 请求

    字段说明:
    - keyword 搜索关键字
    - page_no 分页的页码
    - page_size 分页大小
    - sort 排序方法

    还有其他参数,如果需要可以参见淘宝客api文档: http://baichuan.taobao.com/doc2/detail.htm?spm=a3c0d.7629140.0.0.l7qPEH&treeId=34&articleId=23803&docType=2
    '''
    queryset = QueryRule.objects.all()
    serializer_class = QuerySerializer
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def create(self, request, *args, **kwargs):
        keyword = request.data.get('keyword')
        fields = {}

        if keyword is None:
            data = {'errors': {'code': '400', 'msgs': '您需要输入一个关键字.'}}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        rules = self.queryset.order_by('id')
        # if rules:
        #     for k, v in rules.last().items():
        #         fields[k] = v
        #         # fields = rules if rules else fields


        if rules:
            rules = rules.last()
            columns = [field.column for field in rules._meta.fields]
            for field in columns:
                if hasattr(rules, field) and field != 'id':
                    value = rules.__getattribute__(field)
                    if value:
                        fields[field] = value

        fields['sort'] = request.data.get('sort')
        fields['page_no'] = request.data.get('page_no', 1)
        fields['page_size'] = request.data.get('page_size', 20)

        item = ItemsGet(keyword, rules=fields)

        if item:
            for k, v in enumerate(item):
                item[k]['thumb'] = '%s_%s.jpg' % (v.get('pic_url'), settings.THUMB_LIST)
                item[k]['detail_url'] = reverse('v1.0:goods-detail', request=request, args=[v.get('open_iid')])
                cache.set(v.get('open_iid'), item[k], 60)

        data = {'results': item}

        return Response(data, status=status.HTTP_200_OK)
