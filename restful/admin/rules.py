# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ExportMixin
from reversion.admin import VersionAdmin

from ..models.rules import Rules


class RuleAdmin(ExportMixin, VersionAdmin):
    list_display = ('platform', 'content',)
    list_filter = ('platform',)


# admin.site.register(Rules, RuleAdmin)
