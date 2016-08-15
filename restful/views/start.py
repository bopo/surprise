# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.conf import settings
from django.db.models import Q
from drf_multiple_model.mixins import Query, MultipleModelMixin
from rest_framework import status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

from restful.contrib.consumer.models import UserProfile
from restful.contrib.consumer.serializers import BestsProfileSerializer
from restful.lottery import get_exchange
from restful.models.banner import Banner
from restful.models.bootstrap import Version
from restful.models.goods import Goods
from restful.models.keyword import Keyword
from restful.models.prompt import Prompt
from restful.models.reward import First, FirstPrize
from restful.models.total import Total, Trend
from restful.serializers.banner import BannerSerializer
from restful.serializers.bootstrap import VersionSerializer
from restful.serializers.goods import BestsGoodsSerializer
from restful.serializers.keyword import KeywordSerializer
from restful.serializers.prompt import PromptSerializer
from restful.serializers.start import FirstSerializer
from restful.serializers.total import TotalSerializer, TrendSerializer


class MultipleModelViewSet(MultipleModelMixin, mixins.ListModelMixin, GenericViewSet):
    def get_queryset(self):
        return

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StartViewSet(MultipleModelViewSet):
    '''
    首页各种api合并

    prompt 是抽奖显示文案.

    switch: 切换是否根据购买商品的个数依次增加兑奖天数
    content: 文案显示的内容, 里面需要设置在变量 (:first :second :third)
    forward:
    first: 中一位数字中奖比例
    second: 中两位数字中奖比例
    third: 中三数字中奖比例
    trend_url: 股票大盘网址
    '''

    def get_queryList(self):
        queryList = (
            (Keyword.objects.all(), KeywordSerializer, 'keyword'),
            (Version.objects.all(), VersionSerializer),
            (Banner.objects.all(), BannerSerializer),
            (Total.objects.order_by('id')[:1], TotalSerializer),
            (Trend.objects.filter(exchange=get_exchange()), TrendSerializer),
            (Prompt.objects.all(), PromptSerializer),
        )

        return queryList

    def list(self, request, *args, **kwargs):
        queryList = self.get_queryList()

        # Iterate through the queryList, run each queryset and serialize the data
        results = []

        for query in queryList:
            if not isinstance(query, Query):
                query = Query.new_from_tuple(query)
            # Run the queryset through Django Rest Framework filters
            queryset = self.filter_queryset(query.queryset)

            # If there is a user-defined filter, run that too.
            if query.filter_fn is not None:
                queryset = query.filter_fn(queryset, *args, **kwargs)

            # Run the paired serializer
            context = self.get_serializer_context()
            data = query.serializer(queryset, many=True, context=context).data

            # Get the label, unless add_model_type is note set
            label = None

            if query.label is not None:
                label = query.label
            else:
                if self.add_model_type:
                    label = queryset.model.__name__.lower()

            # if flat=True, Organize the data in a flat manner
            if self.flat:
                for datum in data:
                    if label:
                        datum.update({'type': label})
                    results.append(datum)

            # Otherwise, group the data by Model/Queryset
            else:
                if label:
                    data = {label: data}

                results.append(data)

        if self.flat:
            # Sort by given attribute, if sorting_attribute is provided
            if self.sorting_field:
                results = self.queryList_sort(results)

            # Return paginated results if pagination is enabled
            page = self.paginate_queryList(results)

            if page is not None:
                return self.get_paginated_response(page)

        if request.accepted_renderer.format == 'html':
            return Response({'data': results})

        data = {'trend_url': settings.TREND_URL}

        for result in results:
            # if result.get('total'):
            #     # result.get('total')[0]['exchange'] = get_exchange()
            #     # result.get('total')[0]['exchange'] = result.get('trend')[0].get('exchange')
            #     # result.get('total')[0]['number'] = result.get('trend')[0].get('number')
            #
            #     # if result.get('trend'):
            #     # print result.get('trend')
            #     # result['total'][0]['exchange'] = result['trend'][0]['exchange']
            #     # result['total'][0]['number'] = result['trend'][0]['number']

            data.update(result)

        if data['trend']:
            data['total'][0]['exchange'] = data['trend'][0]['exchange']
            data['total'][0]['number'] = data['trend'][0]['number']

        # del data

        del results

        return Response(data)


class BestsViewSet(MultipleModelViewSet):
    '''
    惊 字餐单的内容,
    百斯特 增加 `saved` 节省金额字段

    - 字段说明:
    best: 打折后的价格
    rate: 返利比例
    rated: 返利比例 小数
    saved: 节省金额
    promotion_price: 淘宝促销金额, 如果此字段不为空 淘宝以此字段为主.
    price: 淘宝原价
    '''

    def get_queryList(self):
        object_ids = [random.randint(0, 200) for _ in range(30)]

        queryList = (
            (Goods.objects.filter(recommend=1)[:90], BestsGoodsSerializer, 'goods'),
            (UserProfile.objects.exclude(avatar__isnull=True).filter(pk__in=object_ids)[:30], BestsProfileSerializer,
            'users'),
        )

        return queryList

    def list(self, request, *args, **kwargs):
        queryList = self.get_queryList()

        # Iterate through the queryList, run each queryset and serialize the data
        results = []

        for query in queryList:
            if not isinstance(query, Query):
                query = Query.new_from_tuple(query)
            # Run the queryset through Django Rest Framework filters
            queryset = self.filter_queryset(query.queryset)

            # If there is a user-defined filter, run that too.
            if query.filter_fn is not None:
                queryset = query.filter_fn(queryset, *args, **kwargs)

            # Run the paired serializer
            context = self.get_serializer_context()
            data = query.serializer(queryset, many=True, context=context).data

            # Get the label, unless add_model_type is note set
            label = None

            if query.label is not None:
                label = query.label
            else:
                if self.add_model_type:
                    label = queryset.model.__name__.lower()

            # if flat=True, Organize the data in a flat manner
            if self.flat:
                for datum in data:
                    if label:
                        datum.update({'type': label})
                    results.append(datum)

            # Otherwise, group the data by Model/Queryset
            else:
                if label:
                    data = {label: data}

                results.append(data)

        if self.flat:
            # Sort by given attribute, if sorting_attribute is provided
            if self.sorting_field:
                results = self.queryList_sort(results)

            # Return paginated results if pagination is enabled
            page = self.paginate_queryList(results)

            if page is not None:
                return self.get_paginated_response(page)

        if request.accepted_renderer.format == 'html':
            return Response({'data': results})

        data = {}

        for result in results:
            data.update(result)

        del results

        return Response(data)


class FirstViewSet(viewsets.GenericViewSet):
    '''
    第一次开机奖励接口
    - 字段说明:
    best: 打折后的价格
    rate: 返利比例
    rated: 返利比例 小数
    saved: 节省金额
    promotion_price: 淘宝促销金额, 如果此字段不为空 淘宝以此字段为主.
    price: 淘宝原价

    - 该接口只接收post方法, 提交后会返回对应的奖励商品数据.
    - 必须登录用户
    - 奖品只能显示一次,如果用户取消则不能再请求,客户端可以缓存到本地存储,如果用户不买,可以重复提示.
    - 提交手机屏幕尺寸或者手机型号,返回一个商品信息的结构.
    - 如下机构
    {
        "open_iid": "AAFsvuLyACLm9G8Glrw1Ypxg",
        "title": "2016夏装新款 透视露肩雪纺裙子喇叭短袖显瘦连衣裙女 D621049L20",
        "pic_url": "http://img01.taobaocdn.com/bao/uploaded/i1/TB1xXlvMXXXXXc9XFXXXXXXXXXX_!!0-item_pic.jpg",
        "shop_type": null,
        "promotion_price": "198.03",
        "price": "439.00",
        "commission_rate": "600.00",
        "saved": "0.00"
    }

    - 手机屏幕尺寸如下:

    ('320x480', "iPhone 4/4S"),
    ('320x568', "iPhone 5/5S/5C"),
    ('375x667', "iPhone 6/6S"),
    ('414x736', "iPhone 6/6S Plus"),

    '''
    queryset = First.objects.all()
    serializer_class = FirstSerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def create(self, request, *args, **kwargs):
        total = self.get_queryset().filter(owner=request.user).count()
        goods = None

        open_iid = None

        if total >= 1:
            raise ValidationError('该用户已经领过奖品')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        # ios 平台判断屏幕尺寸
        if request.data['platform'] == 'ios':
            prize = FirstPrize.objects.filter(
                Q(platform=request.data['platform']) & Q(screensize=request.data['screensize']))[0]

            if prize:
                open_iid = prize.prizegoods

        # 安卓平台判断手机品牌+型号
        if request.data['platform'] == 'android':
            prize = FirstPrize.objects.filter(
                Q(platform=request.data['platform']) &
                Q(phonemodel=request.data['phonemodel'] &
                Q(phonebrand=request.data['phonebrand'])))[0]

            if prize:
                open_iid = prize.prizegoods

        # 没有匹配则找其他赠送商品
        if not open_iid:
            prize = FirstPrize.objects.order_by('?')[0]

            if prize:
                open_iid = prize.prizegoods

        # 判断是否找到赠品
        if open_iid:
            goods = Goods.objects.filter(open_iid=open_iid)[0]

        # 判断是否找到赠品
        if goods:
            serializer = BestsGoodsSerializer(instance=goods, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise ValidationError('没有找到对应商品')

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
