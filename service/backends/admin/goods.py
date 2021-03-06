# -*- coding: utf-8 -*-
from django.contrib import admin
from easy_select2 import select2_modelform
from import_export.admin import ImportExportModelAdmin
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin
from reversion.admin import VersionAdmin
from suit.admin import SortableModelAdmin

from ..models.goods import Goods, GoodsCategory as Category, PreselectionCategory
from ..resources.category import GoodsCategoryResource
from ..resources.goods import GoodsResource


class GoodsAdmin(VersionAdmin, ImportExportModelAdmin):
    resource_class = GoodsResource

    def has_add_permission(self, request):
        pass

    def preview(self, obj):
        return '<img src="%s_64x64.jpg" height="64" width="64" />' % obj.pic_url

    def show_price(self, obj):
        return obj.promotion_price if obj.promotion_price else obj.price

    def commission_rate_(self, obj):
        if obj.commission_rate:
            return '%.1f' % (float(obj.commission_rate) / 100.00) + '%'
        return ' - '

    def commission_price(self, obj):
        if obj.commission:
            return '%.2f' % float(obj.commission)
        return ' - '

    preview.short_description = u'商品图片'
    preview.allow_tags = True

    commission_rate_.short_description = u'比率'
    commission_price.short_description = u'返利'

    list_display = (
        'preview', 'title', 'promotion_price', 'price', 'commission_rate', 'recommend', 'category_recommend',
        'besting')
    list_filter = ('created', 'modified', 'status_changed', 'recommend', 'category', 'category_recommend')
    readonly_fields = ('status_changed', 'created', 'open_iid')
    list_editable = ('category_recommend', 'recommend', 'besting')
    list_display_links = ('title', 'preview')
    search_fields = ('title',)

    def make_recommend(self, request, queryset):
        rows_updated = queryset.update(recommend=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    make_recommend.short_description = u"推荐所选商品"

    def make_unrecommend(self, request, queryset):
        rows_updated = queryset.update(recommend=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    make_unrecommend.short_description = u"取消推荐商品"

    actions = [make_recommend, make_unrecommend, 'delete_selected']


class PreselectionCategoryAdmin(MPTTModelAdmin, SortableModelAdmin):
    form = select2_modelform(PreselectionCategory, attrs={'width': '250px'})

    mptt_level_indent = 20
    sortable = 'ordering'

    search_fields = ('name',)

    list_editable = ('category', 'is_active')
    list_display = ('name', 'source', 'category', 'is_active')
    list_filter = ('source',)


class CategoryAdmin(VersionAdmin, DraggableMPTTAdmin, ImportExportModelAdmin):
    form = select2_modelform(Category, attrs={'width': '250px'})
    resource_class = GoodsCategoryResource
    search_fields = ('name', 'goods__title')
    # list_display = ('name', 'total',)
    # list_display_links = ('name',)
    # list_editable = ('name', 'total')
    # list_filter = ('parent__parent',)


# class TBKCategoryAdmin(VersionAdmin, DraggableMPTTAdmin):
#     mptt_level_indent = 20


# admin.site.register(TBKCategory, TBKCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(PreselectionCategory, PreselectionCategoryAdmin)


