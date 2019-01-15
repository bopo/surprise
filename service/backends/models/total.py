# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class Total(models.Model):
    first = models.IntegerField(_(u'一位数'), default='0')
    second = models.IntegerField(_(u'两位数'), default='0')
    third = models.IntegerField(_(u'三位数'), default='0')
    number = models.IntegerField(_(u'兑奖数字'), default='0')
    exchange = models.DateField(verbose_name=_(u'兑奖时间'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'中奖模拟数据')
        verbose_name_plural = _(u'中奖模拟')


class Trend(models.Model):
    number = models.IntegerField(_(u'大盘数字后三位'), default='0')
    exchange = models.DateField(verbose_name=_(u'兑奖时间'), blank=False, null=False, unique=True, auto_created=now)

    class Meta:
        verbose_name = _(u'大盘走势')
        verbose_name_plural = _(u'大盘走势')
