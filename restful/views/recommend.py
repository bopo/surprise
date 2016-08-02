# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import top
import top.api
from django.conf import settings
from django.core.cache import cache
from django.db.models import Q
from django.utils.timezone import now, timedelta
from django_filters import FilterSet, NumberFilter
from rest_framework import mixins
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from django.f import filters
from rest_framework import filters

from restful.contrib.restauth.settings import TokenSerializer
from restful.models.affairs import Holiday
from restful.models.banner import Banner
from restful.models.goods import Goods, GoodsCategory
from restful.models.prompt import Prompt, Discount
from restful.models.trade import Trade
from restful.serializers.banner import BannerSerializer
from restful.serializers.goods import (GoodsCategorySerializer, GoodsSerializer, GoodsChildrenSerializer,
    TreeCategorySerializer)
from restful.serializers.prompt import PromptSerializer
from restful.serializers.trade import RandomSerializer
from restful.utils import compile_html
from restful.views import BaseViewSet


def get_exchange(user):
    instance = Prompt.objects.first()
    switch__ = instance.switchs if instance else False
    holiday = Holiday.objects.filter(year=now().year)

    total = 1

    if switch__:
        total = Trade.objects.filter(owner=user, created__exact=now()).count()
        total = int(total) + 1

    while True:
        if not holiday:
            break

        forward = now().date() + timedelta(days=+total)

        if str(forward) not in holiday.get().date.split(','):
            break

        total += 1

    # 周六日休市
    weeks = now().isoweekday()
    total += weeks - 5 if weeks > 5 else 0

    return now().date() + timedelta(days=+total)


class SearchFilter(FilterSet):
    min_price = NumberFilter(name="price", lookup_type='gte')
    max_price = NumberFilter(name="price", lookup_type='lte')

    class Meta:
        model = Goods
        # fields = ['category', 'min_price', 'max_price', 'recommend']
        search_fields = ('^name',)
        # lookup_field = '__all__'


class SearchViewSet(viewsets.ReadOnlyModelViewSet, BaseViewSet):
    '''
    增加了mall_item 作为判断是否是天猫商品,返回布尔值,true为天猫商品, 增加详细商品, 字段 detail_url
    排序在过滤器里

    字段代表意义:
        promotion_price 价格
        volume 销量
    参数说明:
        ?ordering=promotion_price 代表正序
        ?ordering=-promotion_price 代表倒序 (字段前面加个 - 代表倒序)
    '''
    # queryset = Goods.objects.filter(delist_time__gt=now())
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    # filter_class = SearchFilter
    search_fields = ('^title',)
    # filter_fields = ('category', 'price')

    filter_fields = ('category',)
    ordering_fields = ('promotion_price', 'volume')
    lookup_field = 'open_iid'

    def get_queryset(self):
        # category = self.request.query_params.get('category')
        #
        # if category:
        #     return self.queryset.filter(category=category)

        return self.queryset

    #
    # def get_object(self):
    #     """
    #     Returns the object the view is displaying.
    #
    #     You may want to override this if you need to provide non-standard
    #     queryset lookups.  Eg if objects are referenced using multiple
    #     keyword arguments in the url conf.
    #     """
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     # Perform the lookup filtering.
    #     lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
    #
    #     assert lookup_url_kwarg in self.kwargs, (
    #         'Expected view %s to be called with a URL keyword argument '
    #         'named "%s". Fix your URL conf, or set the `.lookup_field` '
    #         'attribute on the view correctly.' %
    #         (self.__class__.__name__, lookup_url_kwarg)
    #     )
    #
    #     filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
    #     obj = get_object_or_404(queryset, **filter_kwargs)
    #
    #     # May raise a permission denied
    #     self.check_object_permissions(self.request, obj)
    #
    #     return obj

    # def retrieve(self, request, *args, **kwargs):
    #     self.serializer_class = GoodsDetailSerializer
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        '''
        Args:
            request:
            *args:
            **kwargs:

        Returns:

        '''

        # try:
        #     instance = self.get_object()
        #     self.serializer_class = GoodsDetailSerializer
        #     serializer = self.get_serializer(instance)
        #     return Response(serializer.data)
        # except ObjectDoesNotExist:
        #     data = None
        #
        # if instance is not None:
        # else:

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        item = cache.get(self.kwargs[lookup_url_kwarg])

        if not item:
            instance = self.get_object()
            # self.serializer_class = GoodsDetailSerializer
            self.serializer_class = GoodsSerializer
            serializer = self.get_serializer(instance)

            data = serializer.data
            # data['description'] = compile_html(data['description'])

            return Response(data)

        req = top.api.AtbItemsDetailGetRequest()
        req.set_app_info(top.appinfo(settings.TOP_APPKEY, settings.TOP_SECRET))
        req.fields = "open_iid,cid,title,desc,item_img,pic_url,promotion_price,price"
        req.open_iids = self.kwargs[lookup_url_kwarg]

        try:
            resp = req.getResponse()
            data = resp['atb_items_detail_get_response']['atb_item_details']['aitaobao_item_detail'][0]['item']
        except Exception, e:
            print(e)
            data = {}

        data['item_imgs'] = data['item_imgs']['item_img']
        data['description'] = compile_html(data['desc'])

        for k, v in enumerate(data['item_imgs']):
            data['item_imgs'][k]['url'] = v['url'] + "_" + settings.THUMB_DETAIL + ".jpg"

        del data['desc']

        if item:
            data['promotion_price'] = item['promotion_price']

        return Response(data)


class CategoryTreeViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = GoodsCategory.objects.filter(parent=None, is_active=True)
    serializer_class = TreeCategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    获取商品分类数据

    子分类的调用方法 `/api/v1.0/category/<父分类的ID>/children/` 返回的是该主分类的子分类的列表
    '''

    queryset = GoodsCategory.objects.filter(parent=None, is_active=True)
    serializer_class = GoodsCategorySerializer


class ChildrenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsChildrenSerializer

    def get_queryset(self):
        queryset = self.queryset.prefetch_related('children')
        return queryset

    def list(self, request, category_pk=None):
        queryset = self.get_queryset().filter(parent=category_pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RecommendViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    '''
    # queryset = Goods.objects.filter(recommend=1, delist_time__gt=now()).order_by('ordering')
    queryset = Goods.objects.filter(recommend=1).order_by('ordering')
    # queryset = Goods.objects.filter(recommend=1)
    serializer_class = GoodsSerializer

    # filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    # filter_fields = ('category',)

    def get_queryset(self):
        category = self.request.query_params.get('category')

        if category:
            if category not in ('1', '2', '90'):
                cats = GoodsCategory.objects.filter(id=category).get()

                if cats.parent is None:
                    cats = [x.pk for x in cats.get_children()] if cats else []
                    return self.queryset.filter(Q(category__in=cats))
                else:
                    return self.queryset.filter(category=category)
            elif category in ('1', '2', '90'):
                return self.queryset.filter(category_recommend=category)

        return self.queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        print serializer.data
        return Response(serializer.data)


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.order_by('ordering').all()
    serializer_class = BannerSerializer


class RandomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    新增字段
    trend_url: 股票大盘网址
    '''
    response_serializer = TokenSerializer
    serializer_class = RandomSerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('GET', 'POST', 'OPTIONS', 'HEAD')

    def list(self, request, *args, **kwargs):
        instance = Prompt.objects.first()
        serializer = PromptSerializer(instance)
        data = serializer.data
        price = request.data.get('price', None)

        discount = 0.10

        if price is not None:
            discount = Discount.objects.filter(min_price__lt=price, max_price_gt=price)
            if not discount:
                discount = 0.10

        data['trend_url'] = settings.TREND_URL
        data['discount'] = discount
        data['forward'] = get_exchange(request.user)

        return Response(data)

    def create(self, request, *args, **kwargs):
        try:
            key = request.data.get('key')
            num = Trade.objects.filter(number=key, owner=request.user).count()

            if num >= 1:
                return Response({'errors': {'msgs': '号码重复', 'code': 400}}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'errors': {'msgs': '只允许提交整数', 'code': 400}}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': u'成功.'}, status=status.HTTP_200_OK)
