# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class SharedRule(TimeStampedModel):
    start_date = models.DateField(verbose_name=_(u'开始时间'), blank=False)
    end_date = models.DateField(verbose_name=_(u'过期时间'), blank=False)
    number = models.IntegerField(verbose_name=_(u'分享次数'), default='1')
    price = models.FloatField(verbose_name=_(u'奖励金额'), default='0.00')

    class Meta:
        verbose_name = _(u'分享规则')
        verbose_name_plural = _(u'分享规则')

    def __unicode__(self):
        return '%s-%s' % (self.start_date, self.end_date)

    def __str__(self):
        return self.__unicode__()


class Shared(TimeStampedModel):
    '''
    平台类型 = (('wechat', '微信'), ('weibo', '微博'), ('qq', 'QQ'))
    微信频道 = (('timeline', '朋友圈'), ('friends', '微信好友'))
    分享类型 = (('1', '推广'), ('2', '中奖'), ('3', '提现'))
    '''
    PLATFORM_CHOICES = (('wechat', '微信'), ('weibo', '微博'), ('qq', 'QQ'))
    CHANNELS_CHOICES = (('timeline', '朋友圈'), ('friends', '微信好友'))
    MODEL_CHOICES = (('1', '推广'), ('2', '中奖'), ('3', '提现'))

    platform = models.CharField(verbose_name=_(u'分享平台'), max_length=200, choices=PLATFORM_CHOICES)
    channels = models.CharField(verbose_name=_(u'分享频道'), max_length=200, choices=CHANNELS_CHOICES, blank=True)
    open_iid = models.CharField(verbose_name=_(u'商品开放ID'), max_length=100, default='', help_text=_('非必须,可以为空'))

    model = models.CharField(verbose_name=_(u'分享类型'), max_length=2, choices=MODEL_CHOICES, blank=True, default='')
    title = models.CharField(verbose_name=_(u'商品标题'), max_length=200, blank=True, help_text=_('非必须,可以为空'))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'用户'))

    url = models.URLField(verbose_name=_(u'分享URL'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'分享记录')
        verbose_name_plural = _(u'分享记录')

    def __unicode__(self):
        return self.platform

    def __str__(self):
        return self.__unicode__()
