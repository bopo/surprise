# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import tempfile

import short_url
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.contenttypes import fields as generic
from django.contrib.contenttypes.models import ContentType
from django.core.files import File
from django.db import models
from django.db.models import signals, Sum
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from model_utils import Choices
from model_utils.models import StatusModel, TimeStampedModel
from pilkit.processors import ResizeToFill
from rest_framework.serializers import ValidationError

from restful.models.affairs import Affairs
from restful.utils import createQRCode


def chinese_zodiac(year):
    ''' 生肖函数 '''
    return u'猴鸡狗猪鼠牛虎兔龙蛇马羊'[year % 12]


def zodiac(month, day):
    ''' 星座函数 '''
    n = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
    u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
    d = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
    (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
    return n[len(filter(lambda y: y <= (month, day), d)) % 12]


class AbstractActionType(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, blank=True, default=None)
    content_object = generic.GenericForeignKey('content_type', 'object_id', )

    def validate_unique(self):
        if (self.__class__.objects.filter(owner=self.owner, object_id=self.object_id,
                content_type=self.content_type).exists()):
            raise ValidationError({'detail': 'The record already exists. '})

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password,
            is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()

        if not username:
            raise ValueError('The given username must be set')

        # email = self.normalize_email(email)

        user = self.model(username=username,
            is_staff=is_staff, is_active=True,
            is_superuser=is_superuser,
            date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)


class CustomUser(AbstractUser):
    """
    Concrete class of AbstractEmailUser.
    Use this if you don't need to extend EmailUser.
    """

    REQUIRED_FIELDS = []
    GENDER_CHOICES = (('male', '男'), ('female', '女'))
    mobile = models.CharField(_(u'手机号码'), max_length=25, db_index=True, blank=True)
    verify_code = models.CharField(_(u'短信码'), max_length=5, blank=True)
    device = models.CharField(_(u'设备号'), max_length=100, blank=False, null=False)
    slug = models.UUIDField(_(u'slug'), null=True, blank=True, auto_created=True)
    jpush_registration_id = models.CharField(_(u'jpush_registration_id'), max_length=200, blank=True, null=True)

    # birthday = models.DateField(_(u'生日'), blank=True, null=True)
    # zodiac_zh = models.CharField(_(u'生肖'), max_length=25, blank=True)
    # avatar = models.ImageField(_(u'头像'), max_length=200, blank=True)
    # zodiac = models.CharField(_(u'星座'), max_length=25, blank=True)
    # gender = models.CharField(_(u'性别'), max_length=25, default='male', choices=GENDER_CHOICES)
    # score_total = models.IntegerField(_(u'积分'), default=0)

    objects = CustomUserManager()

    def short(self):
        short_url.encode_url(self.pk)


class Follow(TimeStampedModel):
    '''
    关注
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follows')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='fans')

    def validate_unique(self):
        if (self.__class__.objects.filter(owner=self.owner, to_user=self.to_user).exists()):
            raise ValidationError({'detail': '该用户已经关注过了. '})

    class Meta:
        verbose_name = _(u'关注')
        verbose_name_plural = _(u'关注')


class Extract(TimeStampedModel, StatusModel):
    STATUS = (('ready', '待处理'), ('rejected', '已驳回'), ('success', '已完成'))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    price = models.DecimalField(verbose_name=_(u'提现金额'), max_digits=10, decimal_places=2, null=True)
    alipay = models.CharField(verbose_name=_(u'支付宝'), max_length=100, default='')
    full_name = models.CharField(verbose_name=_(u'用户姓名'), max_length=100, default='')
    is_share = models.BooleanField(verbose_name=_(u'是否分享'), default=False)

    class Meta:
        verbose_name = _(u'提现记录')
        verbose_name_plural = _(u'提现记录')


class Like(AbstractActionType):
    '''
    我喜欢
    '''

    class Meta:
        verbose_name = _(u'我喜欢')
        verbose_name_plural = _(u'我喜欢')


class Signature(TimeStampedModel):
    '''
    签到
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = _(u'签到记录')
        verbose_name_plural = _(u'签到记录')


class Message(TimeStampedModel):
    '''
    用户消息
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    title = models.CharField(verbose_name=_(u'收藏内容的标题'), max_length=255, default='')
    url = models.CharField(verbose_name=_(u'收藏内容的原文地址，不带域名'), max_length=255, default='')
    summary = models.CharField(verbose_name=_(u'收藏内容的描述'), max_length=255, default='')


class Favorite(AbstractActionType):
    '''
    收藏夹
    '''

    class Meta:
        verbose_name = _(u'收藏夹')
        verbose_name_plural = _(u'收藏夹')


class Subscribe(TimeStampedModel):
    """docstring for subscribe"""
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user')

    def validate_unique(self):
        if (self.from_user == self.to_user):
            raise ValidationError({'detail': '不能订阅自己.'})

        if (self.__class__.objects.filter(from_user=self.from_user, to_user=self.to_user).exists()):
            raise ValidationError({'detail': '该用户已经关注过了. '})


class Settings(TimeStampedModel):
    '''
    用户设置
    '''
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, verbose_name=_('user'),
        related_name='settings')
    # gender = models.BooleanField(verbose_name=_(u'gender'), default=1)
    # height = models.FloatField(verbose_name=_(u'height'), max_length=3, null=True)
    # weight = models.FloatField(verbose_name=_(u'weight'), max_length=3, null=True)


class Geographic(TimeStampedModel):
    '''地理位置'''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    latitude = models.FloatField(verbose_name=_(u'latitude'))
    longitude = models.FloatField(verbose_name=_(u'longitude'))

    def __unicode__(self):
        return '%s, %s pos:%s,%s' % (self.owner, self.created, self.latitude, self.longitude)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'User geographic')
        verbose_name_plural = _(u'User geographic')


class Entries(TimeStampedModel):
    '''
    用户登录记录
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    ip = models.GenericIPAddressField(verbose_name=_(u'登录ip'), default='0.0.0.0')
    events = generic.GenericRelation('Behavior')

    # loc = models.OneToOneField(Geographic, null=True)

    def __unicode__(self):
        return '%s %s login.' % (self.owner, self.created)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'登录记录')
        verbose_name_plural = _(u'登录记录')


class Scores(TimeStampedModel):
    '''
    积分
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'credits'))
    event = models.ForeignKey(ContentType, default=0)
    score = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s %s %s' % (self.owner, self.created, self.score)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'积分记录')
        verbose_name_plural = _(u'积分记录')


class UserProfile(TimeStampedModel):
    '''
    该接口更新接受PUT方法

    性别字段英文对应汉字为:
    male:男
    female:女
    提交的数据要用英文.获取时候api也是英文, 要客户端自己做下转换.
    '''
    GENDER_CHOICES = (('male', '男'), ('female', '女'))
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, db_index=True, related_name='profile')
    name = models.CharField(verbose_name=_(u'姓名'), blank=True, max_length=255, db_index=True)
    nick = models.CharField(verbose_name=_(u'昵称'), blank=True, null=True, max_length=255, db_index=True)
    phone = models.CharField(verbose_name=_(u'电话'), default='', blank=True, max_length=64)
    gender = models.CharField(verbose_name=_(u'性别'), max_length=10, choices=GENDER_CHOICES, default=u'male')
    zodiac = models.CharField(_(u'星座'), max_length=25, blank=True)
    birthday = models.DateField(_(u'生日'), blank=True, null=True)
    alipay = models.CharField(verbose_name=_(u'支付宝'), max_length=100, blank=True)
    qq = models.CharField(verbose_name=_(u'QQ'), max_length=100, blank=True)
    chinese_zodiac = models.CharField(_(u'生肖'), max_length=25, blank=True)

    payment = models.DecimalField(verbose_name=_(u'已经提现'), default=0.00, max_digits=10, decimal_places=2)
    balance = models.DecimalField(verbose_name=_(u'帐户余额'), default=0.00, max_digits=10, decimal_places=2)
    total = models.DecimalField(verbose_name=_(u'帐户总额'), default=0.00, max_digits=10, decimal_places=2)

    qrcode = models.ImageField(verbose_name=_(u'二维码'), upload_to='qrcode')
    avatar = ProcessedImageField(verbose_name=_(u'头像'), upload_to='avatar', processors=[ResizeToFill(320, 320)],
        format='JPEG', null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'profile')
        verbose_name_plural = _(u'profiles')


@receiver(signals.post_save, sender=CustomUser)
def sync_profile(instance, created, **kwargs):
    if created:
        slug = '/%s' % short_url.encode_url(instance.pk)
        name = '%s.jpg' % slug
        data = createQRCode(slug)
        temp = tempfile.mktemp()

        data.save(temp, 'JPEG')

        file = open(temp, 'rb')
        data = File(file)

        profile = UserProfile(owner=instance)
        profile.qrcode.save(name=name, content=data, save=True)
        profile.save()

        file.close()

        print "sync profile."

        # if settings.DEBUG:
        #     print 'debug sync do_push_msgs.'
        #     return True
        #
        # try:
        #     notice = Notice.objects.filter(registration=True).get()
        #     do_push_msgs(msgs=notice.title, mobile=instance.mobile, registration_id=instance.registration_id)
        # except Exception, e:
        #     print 'raise do_push_msgs.'
        #     print e.message

        # print 'sync do_push_msgs.'


@receiver(signals.post_save, sender=Affairs)
def post_affairs(instance, created, **kwargs):
    if created:
        print 'created'
        pay = Affairs.objects.filter(owner=instance.owner, pay_type='in').aggregate(Sum('payment'))
        obj, _ = UserProfile.objects.get_or_create(owner=instance.owner)
        obj.total = pay.get('payment__sum')
        obj.save()


class Feedback(TimeStampedModel, StatusModel):
    '''
    用户反馈
    '''
    STATUS = Choices('ready', 'unread', )
    choices = models.CharField(verbose_name=_(u'反馈类型'), max_length=100, null=True)
    content = models.TextField(verbose_name=_(u'反馈内容'), null=True)
    contact = models.CharField(verbose_name=_(u'联系方式'), max_length=200, default='')


class SmsCode(TimeStampedModel, StatusModel):
    '''
    用户短信验证记录
    '''
    STATUS = Choices('open', 'close', )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, verbose_name=_('user'),
        related_name='smscode')
    code = models.CharField(verbose_name=_(u'短信验证码'), max_length=128, unique=True, null=False)


class Address(TimeStampedModel, StatusModel):
    '''
    用户收货地址，将来可能会用
    '''
    STATUS = Choices('open', 'close', )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'用户'))
    full_name = models.CharField(verbose_name=_(u'收信人'), max_length=200, null=False)
    city = models.CharField(verbose_name=_(u'城市'), max_length=200, null=False)
    address = models.CharField(verbose_name=_(u'详细地址'), max_length=200, null=False)
    mobile = models.CharField(verbose_name=_(u'移动电话'), max_length=20, default='0')


class Behavior(AbstractActionType):
    '''用户行为'''

    def __unicode__(self):
        return u"用户:%s, 事件: %s, 时间：%s" % (self.owner, self.content_type, self.created)

    def description(self):
        return self.content_object.description()

    class Meta:
        verbose_name = _(u'用户行为')
        verbose_name_plural = _(u'用户行为')
        ordering = ('created',)
