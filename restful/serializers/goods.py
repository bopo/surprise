# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from restful.models.goods import Goods, GoodsCategory, Preselection
from restful.models.keyword import Keyword


class TreeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name',)


class GoodsCategorySerializer(serializers.ModelSerializer):
    def setup_eager_loading(cls, queryset):
        queryset = queryset.prefetch_related('children')
        return queryset

    class Meta:
        model = GoodsCategory
        fields = ('url', 'id', 'cover', 'name', 'level', 'parent', 'is_active')


class PreselectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preselection


class CollectSerializer(serializers.Serializer):
    key = serializers.CharField(help_text='同步key')
    data = serializers.CharField(help_text='json格式的数据')
    length = serializers.IntegerField(help_text='数据长度,用来校验数据完整性')

    class Meta:
        fields = ('key', 'data', 'length')


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ('id', 'cover', 'name')


class GoodsChildrenSerializer(serializers.ModelSerializer):
    children = ChildrenSerializer(many=True, read_only=True)

    def setup_eager_loading(cls, queryset):
        queryset = queryset.prefetch_related('children')
        return queryset

    class Meta:
        model = GoodsCategory
        # depth = 2
        fields = ('id', 'cover', 'name', 'children')


class BestsGoodsSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(lookup_field='open_iid', view_name='goods-detail')
    pic_url = serializers.CharField(source='thumb')

    class Meta:
        model = Goods
        fields = (
            'open_iid', 'detail_url', 'title', 'pic_url', 'thumb', 'promotion_price', 'price', 'saved', 'rate', 'rated',
            'best')


class FirstGoodsSerializer(serializers.ModelSerializer):
    # saved = serializers.DecimalField(max_digits=10, decimal_places=2, default='')

    class Meta:
        model = Goods
        fields = ('open_iid', 'title', 'pic_url', 'shop_type', 'promotion_price', 'price', 'saved', 'rate', 'best')


class QuerySerializer(serializers.Serializer):
    keyword = serializers.CharField(label=_(u'关键字'))
    page_no = serializers.IntegerField(label=_(u'当前页码'))
    page_size = serializers.IntegerField(label=_(u'每页大小'))
    sort = serializers.CharField(label=_(u'排序方式'))

    class Meta:
        model = Keyword


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods


class GoodsSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(lookup_field='open_iid', view_name='goods-detail')

    class Meta:
        model = Goods
        lookup_field = 'open_iid'
        fields = (
            'detail_url', 'open_iid', 'title', 'price', 'item_imgs', 'promotion_price', 'shop_type', 'pic_url',
            'thumb', 'ordering', 'location')


class GoodsDetailSerializer(serializers.ModelSerializer):
    # detail_url = serializers.HyperlinkedIdentityField(lookup_field='open_iid', view_name='goods-detail')
    # description = serializers.StringRelatedField(source='description.content', read_only=True)
    # item_imgs = serializers.StringRelatedField(source='description.content', read_only=True)

    class Meta:
        model = Goods
        lookup_field = 'open_iid'
        fields = ('open_iid', 'cid', 'title', 'description', 'item_imgs', 'pic_url', 'promotion_price', 'price')

# class GoodsCommentSerializer(serializers.ModelSerializer):
#     # goods = serializers.StringRelatedField()
#     # owner = serializers.StringRelatedField()
#     # owner_id = serializers.ReadOnlyField(source='owner.id')
#     # goods_id = serializers.ReadOnlyField(source='goods.id')
#
#     class Meta:
#         model = GoodsComment
