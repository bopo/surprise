# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ..models.prompt import Discount


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('min_price', 'max_price', 'discount')


admin.site.register(Discount, DiscountAdmin)
