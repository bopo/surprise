# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel

PLATFORM_CHOICES = Choices(
    ('ios', _('IOS')),
    ('android', _('Android')),
    # ('wp', _('Windows Phone')),
    # ('web', _('WEBOS'))
)

CHANNEL_CHOICES = (
    ('1000', "官网"),
    ('1001', "91助手"),
    ('1002', "百度"),
    ('1003', "安卓"),
    ('1004', "豌豆荚"),
    ('1005', "应用宝"),
    ('1006', "360"),
    ('1007', "应用汇"),
    ('1008', "魅族"),
    ('1009', "N多网"),
    ('1010', "PP助手"),
    ('1011', "淘宝"),
    ('1012', "机锋网"),
    ('1013', "金立"),
    ('1014', "小米"),
    ('1015', "华为"),
    ('1016', "搜狗"),
    ('1017', "安智"),
    ('1018', "沃商店"),
    ('1019', "itools"),
    ('1020', "电信爱游戏"),
    ('1021', "优亿市场"),
    ('1022', "应用贝"),
    ('1023', "googleplay"),
    ('1024', "安粉网")
)


class Channel(models.Model):
    name = models.CharField(verbose_name=_(u'渠道名称'), max_length=100, null=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _(u'安装渠道')
        verbose_name_plural = _(u'安装渠道')


class Installation(TimeStampedModel):
    badge = models.IntegerField(verbose_name=_(u'安装标记'))
    timeZone = models.CharField(verbose_name=_(u'设备时区'), max_length=255)
    deviceToken = models.CharField(verbose_name=_(u'设备令牌'), max_length=255)
    installationId = models.CharField(verbose_name=_(u'设备编号'), max_length=255)
    deviceType = models.CharField(verbose_name=_(u'设备类型'), max_length=10, choices=PLATFORM_CHOICES)

    # channel = models.ForeignKey(Channel, verbose_name=_(u'推广渠道'))
    channel = models.CharField(verbose_name=_(u'推广渠道'), max_length=10, blank=False, choices=CHANNEL_CHOICES)

    def __unicode__(self):
        return self.installationId

    def __str__(self):
        return self.installationId

    class Meta:
        verbose_name = _(u'安装统计')
        verbose_name_plural = _(u'安装统计')


class Picture(models.Model):
    pics_url = models.ImageField(verbose_name=_(u'图片'), null=True)
    ordering = models.PositiveIntegerField(verbose_name=_(u'排序'))
    summary = models.CharField(verbose_name=_(u'图片描述'), max_length=200, blank=True)

    class Meta:
        verbose_name = _(u'开机图片')
        verbose_name_plural = _(u'开机图片')


def get_nzb_filename(instance, filename):
    import re

    # if not instance.pk:
    #     instance.save()

    name_slug = re.sub('[^a-zA-Z0-9]', '-', instance.name).strip('-').lower()
    name_slug = re.sub('[-]+', '-', name_slug)
    return u'versions/%s_%s.nzb' % (instance.pk, name_slug)


class Version(TimeStampedModel):
    version = models.CharField(verbose_name=_(u'版本号'), max_length=10, null=False, default='1.0.0')
    install = models.FileField(upload_to='install', verbose_name=_(u'安装连接'), name='install', null=True)
    sha1sum = models.CharField(verbose_name=_(u'文件验证码'), max_length=64, null=False)
    channel = models.CharField(verbose_name=_(u'推广渠道'), max_length=10, blank=False, choices=CHANNEL_CHOICES)
    platform = models.CharField(verbose_name=_(u'APP平台'), max_length=50, default='android', choices=PLATFORM_CHOICES)

    def __unicode__(self):
        return self.version

    def __str__(self):
        return self.version

    def save(self, *args, **kwargs):
        import hashlib
        sha1 = hashlib.sha1()

        for chunk in self.install.chunks():
            sha1.update(chunk)

        self.sha1sum = sha1.hexdigest()
        self.install.name = '%s.apk' % self.sha1sum
        super(Version, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'版本升级')
        verbose_name_plural = _(u'版本升级')


def on_delete(sender, instance, **kwargs):
    instance.install.delete(save=False)


models.signals.post_delete.connect(on_delete, sender=Version)
