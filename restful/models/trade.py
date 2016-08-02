# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Trade(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'登录用户'))
    number = models.CharField(verbose_name=_(u'随机号码'), max_length=10, blank=True, null=True, default=0)
    reward = models.IntegerField(verbose_name=_(u'中奖概率'), blank=True, default=0)
    orderid = models.CharField(verbose_name=_(u'淘宝订单'), max_length=200, default='', unique=True)
    title = models.CharField(verbose_name=_(u'商品标题'), max_length=200, default='')
    pic_url = models.URLField(verbose_name=_(u'图片网址'), default='')
    open_iid = models.CharField(verbose_name=_(u'淘宝商品ID'), max_length=200, default='', help_text=_(u'淘宝开放平台的 open_iid'))
    price = models.DecimalField(verbose_name=_(u'单品价格'), max_digits=10, decimal_places=2, default=0.00)
    nums = models.IntegerField(verbose_name=_(u'购买数量'), blank=True, default=1)
    exchange = models.DateField(verbose_name=_(u'兑奖时间'), blank=True, null=True)
    rebate = models.FloatField(verbose_name=_(u'回扣率'), blank=True, null=True,
        help_text=_(u'区分是随机数,还是折扣商品, 数值为折扣的比例,例如: 0.9 代表九折, 空则为随机数商品'))

    class Meta:
        verbose_name = _(u'交易记录')
        verbose_name_plural = _(u'交易记录')

    def __unicode__(self):
        return self.orderid

    def __str__(self):
        return self.__unicode__()


class Orders(TimeStampedModel):
    number = models.IntegerField(verbose_name=_(u'随机号码'), blank=False, default=0)
    reward = models.IntegerField(verbose_name=_(u'中奖概率'), blank=True, default=0)
    orderid = models.CharField(verbose_name=_(u'淘宝订单'), max_length=200, default='', unique=True)
    title = models.CharField(verbose_name=_(u'商品标题'), max_length=200, default='')
    open_iid = models.CharField(verbose_name=_(u'商品开放id'), max_length=200, default='')
    exchange = models.DateField(verbose_name=_(u'兑奖时间'), blank=True, null=True)

    class Meta:
        verbose_name = _(u'淘宝订单')
        verbose_name_plural = _(u'淘宝订单')

    def __unicode__(self):
        return self.orderid

    def __str__(self):
        return self.__unicode__()
