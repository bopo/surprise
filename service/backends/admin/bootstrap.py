# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from ..models.bootstrap import Version


class VersionsAdmin(VersionAdmin):
    list_display = ('version', 'install', 'platform', 'channel')
    list_filter = ('version', 'channel', 'platform')
    fields = ('version', 'install', 'platform', 'channel')
    actions = ['delete_selected']


admin.site.register(Version, VersionsAdmin)
