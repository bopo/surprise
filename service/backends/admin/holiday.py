# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from ..models.affairs import Holiday


class HolidayAdmin(VersionAdmin):
    list_display = ('year', 'date')


admin.site.register(Holiday, HolidayAdmin)
