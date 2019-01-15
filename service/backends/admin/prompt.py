# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from ..models.prompt import Prompt


class PromptAdmin(VersionAdmin):
    list_display = ('content',)

    def has_delete_permission(self, request, obj=None):
        pass

    def has_add_permission(self, request):
        pass


admin.site.register(Prompt, PromptAdmin)
