# -*- coding: utf-8 -*-
default_app_config = 'restful.contrib.consumer.ConsumerConfig'
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ConsumerConfig(AppConfig):
    name = 'restful.contrib.consumer'
    verbose_name = _(u'用户管理')
