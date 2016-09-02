# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from restful.models.affairs import NoticeTemplate


class NoticeTemplateAdmin(VersionAdmin):
    list_display = ('category', 'subject')
    # def preview(self, obj):
    #     return '<img src="%s" height="64" width="64" />' % obj.cover.url
    #
    # preview.short_description = u'横幅图片'
    # preview.allow_tags = True
    #
    # list_display = ('preview', 'summary', 'click',)
    # list_display_links = ('summary',)
    #
    # search_fields = ('summary',)


admin.site.register(NoticeTemplate, NoticeTemplateAdmin)
