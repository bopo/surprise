# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.timezone import now, timedelta
from django.utils.translation import ugettext_lazy as _
from fabric.colors import *
from model_utils.models import TimeStampedModel

from restful.signals.shared import affairs


class SharedRule(TimeStampedModel):
    EVERY_CHOICES = (('monthly', '每月'), ('weekly', '每周'), ('day', '每天'))
    every = models.CharField(verbose_name=_('分享周期'), max_length=100, choices=EVERY_CHOICES, default=None,
        help_text=_('设置该项,开始时间过期时间不起作用'), blank=True, null=True)
    start_date = models.DateField(verbose_name=_(u'开始时间'), blank=True, null=True)
    end_date = models.DateField(verbose_name=_(u'过期时间'), blank=True, null=True)
    number = models.IntegerField(verbose_name=_(u'分享次数'), default='1')
    price = models.FloatField(verbose_name=_(u'奖励金额'), default='0.00', help_text=_('每次奖励金额'))

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


def shared_rule(owner=None, today=None, rule=None):
    nums = 0
    today = now().date() if today is None else today
    query = Shared.objects.filter(owner=owner, model='1')

    if not rule:
        print 'no rule'
        return False

    if rule.every is not None:

        if rule.every == 'day':  # 每日
            nums = query.filter(created__month=today.month, created__day=today.day).count()
            print owner, green('every day add money +'), rule.price, nums

        if rule.every == 'weekly':  # 每周
            weekday = today.weekday()
            start_date = today + timedelta(days=-weekday)
            end_date = start_date + timedelta(days=6)
            nums = query.filter(created__range=(start_date, end_date)).count()
            print owner, green('every weekly money +'), rule.price, nums

        if rule.every == 'monthly':  # 每月
            nums = query.filter(created__month=today.month).count()
            print owner, green('every monthly money +'), rule.price, nums

        if (nums <= rule.number) & (rule.price > 0.00):
            print owner, green('every add money +'), rule.price
            affairs(owner=owner, price=rule.price, rule=rule)
            return rule.every, nums, rule.price
        else:
            print red('nums > number'), nums

    else:
        nums = query.filter(created__range=(rule.start_date, rule.end_date)).count()
        if (nums <= rule.number) & (rule.price > 0.00):
            print owner, green('add money +'), rule.price
            affairs(owner=owner, price=rule.price, rule=rule)
            return False, nums, rule.price
        else:
            print red('nums > number'), nums

    return False, False, False


def shared_rules(owner, today=None):
    today = now().date() if today is None else today
    rules = SharedRule.objects.all()

    if rules:
        for rule in rules:
            shared_rule(owner=owner, today=today, rule=rule)


@receiver(signals.post_save, sender=Shared)
def sync_shared(instance, created, **kwargs):
    if created:
        shared_rules(owner=instance.owner)
