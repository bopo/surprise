# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from ..models.total import Total


class TotalAdmin(VersionAdmin):
    list_display = ('first', 'second', 'third', 'exchange', 'number')


admin.site.register(Total, TotalAdmin)
