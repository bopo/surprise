# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from .registration import urls as registration_urls
from .views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
    PasswordResetView, SocialView
)

urlpatterns = (
    url(r'^password/reset/$', PasswordResetView.as_view(), name='rest_password_reset'),
    url(r'^password/change/$', PasswordChangeView.as_view(), name='rest_password_change'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^social/$', SocialView.as_view(), name='rest_social_bind'),
    url(r'^registration/', include(registration_urls)),
)
