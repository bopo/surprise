# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from ..models.watchword import Watchword


class WatchwordAdmin(VersionAdmin):
    list_display = ('watchword', 'created')


admin.site.register(Watchword, WatchwordAdmin)
