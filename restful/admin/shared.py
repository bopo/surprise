# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from ..models.shared import Shared, SharedRule


class SharedAdmin(VersionAdmin):
    list_display = ('owner', 'platform', 'channels', 'model', 'url', 'created')
    list_filter = ('platform', 'channels', 'model', 'created')
    ordering = ('-created',)


class SharedRuleAdmin(VersionAdmin):
    list_display = ('every', 'start_date', 'end_date', 'number', 'price')


admin.site.register(Shared, SharedAdmin)
admin.site.register(SharedRule, SharedRuleAdmin)
