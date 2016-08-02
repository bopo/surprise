# -*- coding: utf-8 -*-
from django.contrib import admin

from ..models.scraper import CollectWebsite, GoodsItems


class CollectWebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_', 'scraper')
    list_display_links = ('name',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.url, title=instance.url)

    url_.allow_tags = True


class GoodsItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'collect_website', 'url_',)
    list_display_links = ('title',)
    raw_id_fields = ('checker_runtime',)

    def url_(self, instance):
        return '<a href="{url}" target="_blank">{title}</a>'.format(
            url=instance.detail_url, title=instance.detail_url)

    url_.allow_tags = True


admin.site.register(CollectWebsite, CollectWebsiteAdmin)
admin.site.register(GoodsItems, GoodsItemsAdmin)
