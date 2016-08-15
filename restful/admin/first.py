# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from easy_select2 import select2_modelform
from reversion.admin import VersionAdmin

from ..models.reward import FirstPrize


class FirstPrizeAdmin(VersionAdmin):
    # form = select2_modelform(FirstPrize, attrs={'width': '250px'})
    # search_fields = ('name', 'goods__title')
    list_display_links = ('prizegoods',)
    list_display = ('platform', 'screensize', 'phonebrand', 'phonemodel', 'prizegoods', 'location',)


admin.site.register(FirstPrize, FirstPrizeAdmin)
