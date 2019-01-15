# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import TradeViewSet, AffairsViewSet, NoticeViewSet, SharedViewSet, ProfileViewSet, AvatarViewSet, \
    ExtractViewSet

router = DefaultRouter()
router.register(r'notices', NoticeViewSet, 'me-messages')
router.register(r'affairs', AffairsViewSet, 'me-affairs')
router.register(r'extract', ExtractViewSet, 'me-extract')
router.register(r'shared', SharedViewSet, 'me-shared')
router.register(r'orders', TradeViewSet, 'me-trade')

urlpatterns = (
    url(r'^', include(router.urls)),
    url(r'^profile/$', ProfileViewSet.as_view(), name='me-profile'),
    url(r'^avatar/$', AvatarViewSet.as_view(), name='me-avatar'),
)
