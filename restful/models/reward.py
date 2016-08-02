# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from restful.models.bootstrap import PLATFORM_CHOICES
from restful.models.goods import Goods


class Reward(models.Model):
    value = models.CharField(verbose_name=_(u'大盘指数'), max_length=20, blank=False)
    today = models.DateField(verbose_name=_(u'指数日期'), blank=False)

    class Meta:
        verbose_name = _(u'指数记录')
        verbose_name_plural = _(u'指数记录')

    def __unicode__(self):
        return self.keyword

    def __str__(self):
        return self.__unicode__()


class First(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'所属用户'), blank=True, null=True)
    platform = models.CharField(verbose_name=_(u'APP平台'), max_length=50, default='android', choices=PLATFORM_CHOICES)
    location = models.CharField(verbose_name=_(u'地址信息'), max_length=200, blank=False)
    coordinate = models.CharField(verbose_name=_(u'位置坐标'), max_length=200, blank=False)
    screensize = models.CharField(verbose_name=_(u'屏幕尺寸'), max_length=200, blank=False)

    class Meta:
        verbose_name = _(u'首登奖励')
        verbose_name_plural = _(u'首登奖励')

    def __unicode__(self):
        return self.owner

    def __str__(self):
        return self.__unicode__()


SCREENSIZE_CHOICES = (
    ('320x480', "iPhone 4/4S"),
    ('320x568', "iPhone 5/5S/5C"),
    ('375x667', "iPhone 6/6S"),
    ('414x736', "iPhone 6/6S Plus"),
)


class FirstPrize(models.Model):
    platform = models.CharField(verbose_name=_(u'APP平台'), max_length=50, default='android', choices=PLATFORM_CHOICES)
    location = models.CharField(verbose_name=_(u'地址信息'), max_length=200, blank=True, null=True)
    coordinate = models.CharField(verbose_name=_(u'位置坐标'), max_length=200, blank=True, null=True)
    screensize = models.CharField(verbose_name=_(u'屏幕尺寸'), max_length=200, blank=False, choices=SCREENSIZE_CHOICES)
    prizegoods = models.ForeignKey(Goods, verbose_name=_(u'对应奖品'), blank=True, null=True)
    phonemodel = models.CharField(verbose_name=_(u'手机型号'), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _(u'首登奖品')
        verbose_name_plural = _(u'首登奖品')

    def __unicode__(self):
        return '%s %s' % (self.platform, self.phonemodel)

    def __str__(self):
        return self.__unicode__()
