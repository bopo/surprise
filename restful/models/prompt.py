# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class SharePrompt(models.Model):
    content = models.TextField(verbose_name=_(u'分享提示'), blank=False)


class Prompt(models.Model):
    switch2 = models.BooleanField(verbose_name=_(u'购买规则'), default=0)
    content = models.TextField(verbose_name=_(u'规则提示'), blank=False)
    forward = models.DateField(verbose_name=_(u'开奖时间'), blank=True, null=True)
    first_msg = models.CharField(verbose_name=_(u'一位中奖提示'), max_length=200, default='')
    second_msg = models.CharField(verbose_name=_(u'两位中奖提示'), max_length=200, default='')
    third_msg = models.CharField(verbose_name=_(u'三位中奖提示'), max_length=200, default='')
    first_rate = models.DecimalField(verbose_name=_(u'一位中奖比率'), max_digits=10, decimal_places=2, null=True)
    second_rate = models.DecimalField(verbose_name=_(u'两位中奖比率'), max_digits=10, decimal_places=2, null=True)
    third_rate = models.DecimalField(verbose_name=_(u'三位中奖比率'), max_digits=10, decimal_places=2, null=True)

    @property
    def switchs(self):
        return '1' if self.switch2 else '0'

    class Meta:
        verbose_name = _(u'提示文案')
        verbose_name_plural = _(u'提示文案')

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.__unicode__()


class Discount(models.Model):
    min_price = models.DecimalField(_(u'最小价格'), max_digits=10, decimal_places=2, default='0.00')
    max_price = models.DecimalField(_(u'最大价格'), max_digits=10, decimal_places=2, default='0.00')
    discount = models.DecimalField(_(u'中奖比率'), max_digits=10, decimal_places=2, default='0.00')

    class Meta:
        verbose_name = _(u'中奖比率')
        verbose_name_plural = _(u'中奖比率')

    def __unicode__(self):
        return '%.2f' % self.discount

    def __str__(self):
        return self.__unicode__()

# class Settings(django_settings.db.Model):
#     value = models.TextField()
#
#     class Meta:
#         abstract = True
#
#
# django_settings.register(Settings)
