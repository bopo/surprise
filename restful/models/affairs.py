# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jpush
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import StatusModel, TimeStampedModel

from restful.helpers import do_push_msgs


class Affairs(StatusModel):
    STATUS = Choices(('ready', u'未提现'), ('done', u'已提现'))
    PAY_TYPE = Choices(('in', u'收入'), ('out', u'支出'))

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'用户'))
    orderid = models.CharField(verbose_name=_(u'淘宝订单'), max_length=100, default='', unique=True)
    payment = models.DecimalField(verbose_name=_(u'发生额'), default=0.00, max_digits=10, decimal_places=2)
    created = models.DateTimeField(verbose_name=_(u'发生时间'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_(u'操作时间'), blank=True, auto_now=True)
    pay_type = models.CharField(verbose_name=_(u'收支类型'), max_length=20, choices=PAY_TYPE, default='in')

    class Meta:
        ordering = ('pk',)
        verbose_name = _(u'财务记录')
        verbose_name_plural = _(u'财务记录')

    def __unicode__(self):
        return '%s: %s' % (self.owner, self.payment)

    def __str__(self):
        return self.__unicode__()


class NoticeTemplate(models.Model):
    CATEGORY_CHOICES = (
        ('reward', "中奖消息"),
        ('signup', "注册消息"),
        ('system', "系统消息"),
        ('payment', "支付消息"),
        ('confirm', "商品确认"),
    )

    category = models.CharField(verbose_name=_(u'消息模板分类'), max_length=255, default='', choices=CATEGORY_CHOICES)
    subject = models.CharField(verbose_name=_(u'消息模板标题'), max_length=255, default='')
    content = models.TextField(verbose_name=_(u'消息模板正文'), default='')

    def __unicode__(self):
        return self.subject

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'消息模板')
        verbose_name_plural = _(u'消息模板')


class Notice(TimeStampedModel):
    '''
    用户消息
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name=_(u'推送给用户'))
    is_top = models.BooleanField(verbose_name=_(u'消息置顶'), default=False)
    registration = models.BooleanField(verbose_name=_(u'注册成功推送的消息'), default=False,
        help_text=_(u'注册成功后发送的消息,只能有一条. 用户设置为空, 必须为置顶'))
    title = models.CharField(verbose_name=_(u'消息标题'), max_length=255, default='')
    content = models.TextField(verbose_name=_(u'消息正文'), default='')
    template = models.CharField(verbose_name=_(u'模板名称'), max_length=255, default='default', unique=True)

    # def push(self, *args, **kwargs):
    #     msgs = self.title
    #     push = jpush.JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    #     push = push.create_push()
    #
    #     extras = {'mobile': self.owner.mobile}
    #     push.notification = jpush.notification(alert=msgs)
    #     push.options = {"time_to_live": 86400, "apns_production": True, 'extras': extras}
    #     push.audience = jpush.audience(
    #         jpush.registration_id(self.owner.registration_id)) if self.owner.registration_id else jpush.all_
    #     push.platform = jpush.all_
    #     push.send()
    #
    #     return True

    def __unicode__(self):
        return '%s: %s' % (self.owner, self.title)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        ordering = ('pk',)
        verbose_name = _(u'用户消息')
        verbose_name_plural = _(u'用户消息')


class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    event = GenericForeignKey('content_type', 'object_id')
    created = models.DateTimeField(u'事件发生时间', auto_now_add=True)

    def __unicode__(self):
        return u"%s的事件: %s" % (self.user, self.description())

    def description(self):
        return self.event.description()


class Holiday(models.Model):
    year = models.CharField(verbose_name=_(u'年份'), max_length=10, unique=True, default='2016')
    date = models.TextField(verbose_name=_(u'休市日期集合'), help_text=_(u'多个用逗号分开.'), null=True)

    def save(self, *args, **kwargs):
        self.date = self.date.strip().replace(u'，', ',').strip(',')
        super(self.__class__, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s的股市休市日期" % self.year

    def __str__(self):
        self.__unicode__()

    class Meta:
        ordering = ('-year',)
        verbose_name = _(u'休市日期')
        verbose_name_plural = _(u'休市日期')


@receiver(post_save, sender=Notice)
def signal_receiver_notice(instance, created, **kwargs):
    mobile, registration_id = (None, None)

    if created is True:
        if instance.owner:
            mobile = instance.owner.mobile
            registration_id = instance.owner.jpush_registration_id if instance.owner.jpush_registration_id else None

        do_push_msgs(msgs=instance.title, mobile=mobile, registration_id=registration_id)

        print instance.title
        print "sync_push."
