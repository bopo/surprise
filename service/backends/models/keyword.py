# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Keyword(TimeStampedModel):
    keyword = models.CharField(verbose_name=_(u'关键词'), max_length=200, default='')

    class Meta:
        verbose_name = _(u'搜索热词')
        verbose_name_plural = _(u'搜索热词')

    def __unicode__(self):
        return self.keyword

    def __str__(self):
        return self.__unicode__()
