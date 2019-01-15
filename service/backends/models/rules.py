# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel

PLATFORM_CHOICES = Choices(('ios', _('IOS')), ('android', _('Android')))


class Rules(TimeStampedModel):
    platform = models.CharField(verbose_name=_(u'手机平台'), max_length=200, blank=True, choices=PLATFORM_CHOICES)
    content = models.TextField(verbose_name=_(u'淘口令规则'), default='', unique=True)

    class Meta:
        verbose_name = _(u'口令规则')
        verbose_name_plural = _(u'口令规则')


def __unicode__(self):
    return self.platform


def __str__(self):
    return self.__unicode__()
