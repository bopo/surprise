# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import short_url
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_filters import FilterSet
from rest_framework import serializers
from rest_framework import status, viewsets, filters
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from restful.models.affairs import Affairs, Notice
from restful.models.shared import Shared, SharedRule
from restful.models.trade import Trade
from restful.serializers.shared import SharedSerializer, QRCodeSerializer
from restful.serializers.trade import TradeSerializer
from .models import Feedback, UserProfile
from .serializers import (
    AddressSerializer, FeedbackSerializer, ProfileSerializer, AffairsSerializer, NoticeSerializer, AvatarSerializer,
    ExtractSerializer)
from .utils import get_user_profile


class AffairsFilter(FilterSet):
    class Meta:
        model = Affairs
        fields = ('pay_type', 'status')
        # search_fields = ('^name',)
        # ordering_fields = '__all__'


class AffairsViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    该接口是我的钱包,收支列表
    pay_type 支付类型, (('in', '收入'), ('out', '支出'))
    status 提现状态 ('ready', '未提现'), ('done', '已提现')
    '''
    queryset = Affairs.objects.all()
    serializer_class = AffairsSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AffairsFilter
    filter_fields = '__all__'

    allowed_methods = ('GET', 'OPTIONS', 'HEAD')

    def get_object(self):
        return self.request.user.affairs_set.all()

    def get_queryset(self):
        return self.request.user.affairs_set.all()


class ExtractViewSet(viewsets.ModelViewSet):
    '''
    is_share 是否提现前已经做了微信分享,这个客户端判断, 是为true,不是则为 flase 都为字符串类型
    price 提现金额不能超出用户的余额

    之前有未完成的提现,不能重复提现,接口会做相应的提醒。
    '''
    serializer_class = ExtractSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        owner = UserProfile.objects.filter(owner=request.user).get()
        ready = self.get_queryset().filter(status='ready')

        # if not owner.alipay:
        #     raise serializers.ValidationError("支付宝账户不存在.")

        if owner.balance <= request.data['price']:
            raise serializers.ValidationError("提现金额超出您的余额.")

        if ready:
            raise serializers.ValidationError("已经有一笔未完成的提现,待完成后才可继续提现.")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.request.user.extract_set.all()


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class ProfileViewSet(RetrieveUpdateAPIView):
    '''
    用户信息
    '''
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        # slug = self.request.user.slug.hex if self.request.user.slug else None
        data['slug'] = short_url.encode_url(instance.pk)
        data['qrcode'] = reverse('frontend.views.q', args=[data['slug']], request=request)
        return Response(data)

    def get_object(self):
        return get_user_profile(self.request.user)


class TradeViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    这个接口是用来接收APP购买成功后返回的信息.

    字段待定...
    '''
    # queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.trade_set.filter(confirmed__isnull=False)
        # return self.request.user.trade_set.all()


class AvatarViewSet(RetrieveUpdateAPIView):
    '''
    头像上传接口.

    '''
    serializer_class = AvatarSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_user_profile(self.request.user)


class NoticeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NoticeSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return Notice.objects.filter((Q(owner=self.request.user.pk) | Q(owner=None)))

    def get_queryset(self):
        return Notice.objects.filter((Q(owner=self.request.user.pk) | Q(owner=None)))


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.address_set.all()


class SharedViewSet(viewsets.ModelViewSet):
    '''
    选择性数据字典(对应中文的关系):

    平台类型 = (('wechat', '微信'), ('weibo', '微博'), ('qq', 'QQ'))
    微信频道 = (('timeline', '朋友圈'), ('friends', '微信好友'))
    分享类型 = (('1', '推广'), ('2', '中奖'), ('3', '提现'))
    '''

    serializer_class = SharedSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.request.user.shared_set.all()


class QRCodeViewSet(viewsets.ModelViewSet):
    '''
    二维码生成:
    '''

    serializer_class = QRCodeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.request.user.shared_set.all()


@receiver(post_save, sender=Shared)
def shared_handler(sender, **kwargs):
    instance = kwargs['instance']
    rules = SharedRule.objects.order_by('-id').last()

    if rules is not None:
        count = Shared.objects.filter(owner=instance.owner, created__range=(rules.start_date, rules.end_date)).count()
        if rules.number == count:
            Affairs.objects.get_or_create(
                owner=instance.owner,
                payment=rules.price
            )

            # event = Event(user=instance.owner, event=instance)
            # event.save()

            # 推送事件
            # 写入`notice`表
            notice = Notice(owner=instance.owner, title=u'您有一笔新的入账',
                content=u'分享奖励: 您分享了%s次,获得%s奖励' % (rules.number, rules.price))
            notice.save()

    print "Request finished!"
