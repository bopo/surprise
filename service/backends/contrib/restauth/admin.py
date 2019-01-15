# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import HTML5Input, SuitSplitDateTimeWidget

from .models import *


class VerifyCodeForm(ModelForm):
    class Meta:
        model = VerifyCode
        widgets = {
            'created': SuitSplitDateTimeWidget,
            'mobile': HTML5Input(input_type='number'),
        }
        exclude = ('status_changed', 'code')


class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'code', 'status', 'created')
    form = VerifyCodeForm

    def has_add_permission(self, request):
        pass

    def has_delete_permission(self, request, obj=None):
        pass


admin.site.register(VerifyCode, VerifyCodeAdmin)
