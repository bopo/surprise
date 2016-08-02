# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from easy_select2 import select2_modelform
from reversion.admin import VersionAdmin

from ..contrib.consumer.models import Extract
from ..forms.affairs import AffairsForm
from ..models.affairs import Affairs, Notice


class AffairsAdmin(VersionAdmin):
    form = AffairsForm
    # readonly_fields = ('payment', 'owner', 'created', 'modified', 'status', 'status_changed')
    list_display = ('payment', 'owner', 'created', 'modified', 'pay_type', 'status')
    list_filter = ('owner', 'status', 'created')

    # def has_add_permission(self, request):
    #     pass
    #
    # def has_delete_permission(self, request, obj=None):
    #     pass
    #
    # def save_model(self, request, obj, form, change):
    #     pass


admin.site.register(Affairs, AffairsAdmin)


class NoticeAdmin(VersionAdmin):
    # form = NoticeForm
    form = select2_modelform(Notice, attrs={'width': '250px'})
    list_display = ('owner', 'title', 'created', 'modified', 'is_top', 'registration')
    list_filter = ('owner', 'is_top', 'registration', 'created')


admin.site.register(Notice, NoticeAdmin)


class ExtractAdmin(VersionAdmin):
    list_display = ('owner', 'price', 'is_share', 'status', 'created', 'status_changed')

    def has_add_permission(self, request):
        pass

    def make_rejected(self, request, queryset):
        rows_updated = queryset.update(status='rejected')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='success')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    make_rejected.short_description = u"驳回选中的提现"
    make_published.short_description = u"完成选中的提现"

    actions = [make_rejected, make_published]


admin.site.register(Extract, ExtractAdmin)
