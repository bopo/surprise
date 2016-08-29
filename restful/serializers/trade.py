# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from restful.models.trade import Trade


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('number', 'orderid', 'title', 'open_iid', 'nums', 'price', 'reward', 'exchange', 'pic_url', 'rebate',
        'confirmed')


class RandomSerializer(serializers.Serializer):
    key = serializers.CharField(required=True, allow_blank=True, label=_(u'随机数'))
