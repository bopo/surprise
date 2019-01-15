# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'restful.RestfulConfig'


class RestfulConfig(AppConfig):
    name = 'restful'
    verbose_name = _(u'API资源')
