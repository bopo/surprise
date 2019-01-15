# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework.reverse import reverse

from restful.models.goods import Goods
from restful.models.reward import First
from restful.serializers.banner import BannerSerializer
from restful.serializers.bootstrap import VersionSerializer
from restful.serializers.keyword import KeywordSerializer
from restful.serializers.rules import RulesSerializer


class StartSerializer(serializers.Serializer):
    keyword = KeywordSerializer
    version = VersionSerializer
    banner = BannerSerializer
    rules = RulesSerializer

    class Meta:
        fields = ('banner', 'keyword', 'rules', 'version')


class CustomerHyperlink(serializers.HyperlinkedRelatedField):
    # We define these as class attributes, so we don't need to pass them as arguments.
    view_name = 'goods-detail'
    queryset = Goods.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'organization_slug': obj.prizegoods.open_iid,
            'goods_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'organization__slug': view_kwargs['organization_slug'],
            'pk': view_kwargs['goods_pk']
        }
        return self.get_queryset().get(**lookup_kwargs)


# class FirstPrizeSerializer(serializers.ModelSerializer):
#     title = serializers.StringRelatedField(source='prizegoods.title')
#     pic_url = serializers.StringRelatedField(source='prizegoods.pic_url')
#     price = serializers.StringRelatedField(source='prizegoods.price')
#     detail_url = CustomerHyperlink()
#
#     class Meta:
#         model = FirstPrize
#         fields = ('platform', 'coordinate', 'screensize', 'title', 'pic_url', 'price', 'detail_url')


class FirstSerializer(serializers.ModelSerializer):
    class Meta:
        model = First
        fields = ('platform', 'coordinate', 'screensize', 'phonebrand', 'phonemodel')
