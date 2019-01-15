# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Start(models.Model):
    summary = models.CharField(verbose_name=_(u'描述'), max_length=100, default='')

    # click = models.URLField(verbose_name=_(u'网址'), default='')
    # cover = models.ImageField(_(u'图片'), blank=True)
    # ordering = models.IntegerField(_(u'排序'), default='1')

    class Meta:
        ordering = ('pk',)
        verbose_name = _(u'横幅广告')
        verbose_name_plural = _(u'横幅广告')

    def __unicode__(self):
        return self.summary

    def __str__(self):
        return self.__unicode__()
