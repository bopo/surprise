# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from reversion.admin import VersionAdmin

from restful.resources.firstprize import FirstPrizeResource
from ..models.reward import FirstPrize


class FirstPrizeAdmin(ImportExportModelAdmin, VersionAdmin):
    resource_class = FirstPrizeResource
    # form = select2_modelform(FirstPrize, attrs={'width': '250px'})
    # search_fields = ('name', 'goods__title')
    list_display_links = ('prizegoods',)
    list_display = ('platform', 'screensize', 'phonebrand', 'phonemodel', 'prizegoods', 'location',)


admin.site.register(FirstPrize, FirstPrizeAdmin)
