# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# class Admin(admin.ModelAdmin):
#     def preview(self, obj):
#         return '<img src="%s" height="64" width="64" />' % obj.cover
#
#     preview.short_description = u'横幅图片'
#     preview.allow_tags = True
#
#     list_display = ('preview', 'summary', 'click',)
from reversion.admin import VersionAdmin

from restful.models.goods import QueryRule

admin.site.register(QueryRule, VersionAdmin)
