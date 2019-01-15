# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'restful.contrib.restauth.RestauthConfig'


class RestauthConfig(AppConfig):
    name = 'restful.contrib.restauth'
    verbose_name = _(u'Restful 认证')
