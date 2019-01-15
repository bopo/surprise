# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Watchword(TimeStampedModel):
    CHOICES_SORT = (('price_asc', '价格升序'), ('price_desc', '价格倒序'))
    watchword = models.TextField(verbose_name=_(u'口令'), max_length=200, default='')
    sort = models.CharField(verbose_name=_(u'排序方式'), max_length=20, default='price_asc', choices=CHOICES_SORT)

    class Meta:
        verbose_name = _(u'淘客口令')
        verbose_name_plural = _(u'淘客口令')

    def __unicode__(self):
        return self.watchword

    def __str__(self):
        return self.__unicode__()
