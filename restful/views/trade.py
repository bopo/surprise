# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from restful.helpers import DetailGet
from restful.lottery import set_exchange
from restful.models.goods import Goods
from restful.models.trade import Trade
from restful.serializers.trade import TradeSerializer


def get_picurl(open_iid):
    if not open_iid:
        return None

    try:
        result = Goods.objects.filter(open_iid=open_iid)
        return result.get().pic_url
    except Goods.DoesNotExist:
        pass

    # @API获取数据
    result = DetailGet(open_iid)
    return result['pic_url'] if result else None


class TradeViewSet(mixins.CreateModelMixin, GenericViewSet):
    '''
    这个接口是用来接收APP购买成功后返回的信息. "需要登录权限"

    订单号为唯一,如果提交时候订单号不是唯一会抛出异常,则不用理会.

    - 增加一个字段 `rebate` 用区分是随机数还是折扣商品; 数值为折扣的比例,例如: 0.9 代表九折, 空则为随机数商品.
    '''
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('POST', 'HEAD', 'OPTIONS')

    def perform_create(self, serializer):
        # @todo 获取商品信息, 更新交易表
        pic_url = get_picurl(self.request.data['open_iid'])
        serializer.save(owner=self.request.user, pic_url=pic_url, exchange=set_exchange(self.request.user))
