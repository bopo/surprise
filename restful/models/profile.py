# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

#
# class Profile(TimeStampedModel):
#     GENDER_CHOICES = (('male', '男'), ('female', '女'))
#
#     owner = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, db_index=True)
#     fullname = models.CharField(verbose_name=_(u'姓名'), blank=True, max_length=255, db_index=True)
#     mobile = models.CharField(verbose_name=_(u'手机号'), default='', blank=True, max_length=64)
#     gender = models.CharField(verbose_name=_(u'性别'), max_length=10, choices=GENDER_CHOICES, default=u'male')
#     zodiac = models.CharField(verbose_name=_(u'生肖'), max_length=25, blank=True)
#     birthday = models.DateField(verbose_name=_(u'生日'), blank=True, null=True)
#
#     def __unicode__(self):
#         return self.name
#
#     def __str__(self):
#         return self.__unicode__()
#
#     class Meta:
#         verbose_name = _(u'profile')
#         verbose_name_plural = _(u'profiles')
