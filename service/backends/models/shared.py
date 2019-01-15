# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.timezone import now, timedelta
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from restful.signals.shared import affairs


class SharedRule(TimeStampedModel):
    EVERY_CHOICES = (('monthly', '每月'), ('weekly', '每周'), ('day', '每天'))

    dayly = models.IntegerField(verbose_name=_('每日次数'), blank=True, null=True, default=None)
    weekly = models.IntegerField(verbose_name=_('每周次数'), blank=True, null=True, default=None)
    monthly = models.IntegerField(verbose_name=_('每月次数'), blank=True, null=True, default=None)

    # every = models.CharField(verbose_name=_('分享周期'), max_length=100, choices=EVERY_CHOICES, default=None,
    #     help_text=_('设置该项,开始时间过期时间不起作用'), blank=True, null=True)

    start_date = models.DateField(verbose_name=_(u'开始时间'), blank=True, null=True)
    end_date = models.DateField(verbose_name=_(u'过期时间'), blank=True, null=True)

    reg_start_date = models.DateField(verbose_name=_(u'注册开始时间'), blank=True, null=True)
    reg_end_date = models.DateField(verbose_name=_(u'注册结束时间'), blank=True, null=True)

    price = models.FloatField(verbose_name=_(u'每次奖励'), default='0.00', help_text=_('每次奖励金额'))

    # number = models.IntegerField(verbose_name=_(u'分享次数'), default='1')

    class Meta:
        verbose_name = _(u'分享规则')
        verbose_name_plural = _(u'分享规则')

    def __unicode__(self):
        return '%s -- %s' % (self.start_date, self.end_date)

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
    effective = models.BooleanField(verbose_name=_(u'已经激活'), default=False)

    class Meta:
        verbose_name = _(u'分享记录')
        verbose_name_plural = _(u'分享记录')

    def __unicode__(self):
        return self.platform

    def __str__(self):
        return self.__unicode__()


def weekday(today):
    weekday = today.weekday()
    start_date = today + timedelta(days=-weekday)
    end_date = start_date + timedelta(days=6)
    return start_date, end_date


def shared_rule(owner=None, today=None, rule=None, instance=None):
    today = now().date() if today is None else today
    query = Shared.objects.filter(owner=owner, model='1', effective=1)

    # 条件
    # 判断时间
    if rule.start_date:
        query.filter(created__gt=rule.start_date)

    if rule.end_date:
        query.filter(created__lt=rule.end_date)

    # 判断注册时间
    if rule.reg_start_date:
        query.filter(owner__date_joined__gt=rule.reg_start_date)

    if rule.reg_end_date:
        query.filter(owner__date_joined__lt=rule.reg_end_date)

    monthly = query.filter(created__month=today.month).count()

    if rule.monthly > monthly:
        print 'monthly pass', monthly, rule.monthly
        weekly = query.filter(created__range=weekday(today)).count()

        if rule.weekly > weekly:
            print 'weekly pass', weekly, rule.weekly
            dayly = query.filter(created__month=today.month, created__day=today.day).count()

            if rule.dayly > dayly:
                print 'dayly pass', 'affairs', dayly, rule.dayly
                affairs(owner=owner, price=rule.price, rule=rule)

                instance.effective = 1
                instance.save()
            else:
                print 'dayly err'
        else:
            print 'weekly err'
    else:
        print 'monthly err'


def shared_rules(owner, instance=None, today=None):
    today = now().date() if today is None else today
    rules = SharedRule.objects.order_by('id').last()
    shared_rule(owner=owner, today=today, rule=rules, instance=instance)


@receiver(signals.post_save, sender=Shared)
def sync_shared(instance, created, **kwargs):
    if created:
        shared_rules(owner=instance.owner, instance=instance)
