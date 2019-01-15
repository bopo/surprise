# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from ..models.keyword import Keyword


class KetwordAdmin(VersionAdmin):
    list_display = ('keyword', 'created')


admin.site.register(Keyword, KetwordAdmin)
