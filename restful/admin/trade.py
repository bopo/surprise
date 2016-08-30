# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ExportMixin, ImportMixin
from reversion.admin import VersionAdmin

from ..models.trade import Trade


class TradeAdmin(ExportMixin, VersionAdmin):
    list_display = ('orderid', 'owner', 'number', 'reward', 'rebate', 'created', 'confirmed')
    # readonly_fields = ('orderid', 'open_iid', 'owner',)
    list_filter = ('owner', 'created')

    # def has_add_permission(self, request):
    #     pass
    #
    # def has_delete_permission(self, request, obj=None):
    #     pass
    #
    # def save_model(self, request, obj, form, change):
    #     pass


class OrdersAdmin(ImportMixin, VersionAdmin):
    list_display = ('orderid', 'created')
    # readonly_fields = ('orderid',)
    list_filter = ('created',)


admin.site.register(Trade, TradeAdmin)
# admin.site.register(Orders, OrdersAdmin)
