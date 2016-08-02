# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


class ConfigAdmin(admin.ModelAdmin):
    pass
    # def preview(self, obj):
    #     return '<img src="%s" height="64" width="64" />' % obj.cover
    #
    # preview.short_description = u'横幅图片'
    # preview.allow_tags = True
    #
    # list_display = ('preview', 'summary', 'click',)

# admin.site.register(Banner, ConfigAdmin)
