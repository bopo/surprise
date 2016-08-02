# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Location(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'登录用户'), blank=True, null=True)
    imei = models.CharField(verbose_name=_(u'设备号码'), max_length=100, blank=False, null=False, default='')
    address = models.CharField(verbose_name=_(u'详细地址'), max_length=200, blank=True)
    coordinate = models.CharField(verbose_name=_(u'位置坐标'), max_length=200, default='')

    class Meta:
        verbose_name = _(u'位置信息')
        verbose_name_plural = _(u'位置信息')


def __unicode__(self):
    return '%s %s' % (self.owner, self.address)


def __str__(self):
    return self.__unicode__()
