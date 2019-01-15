# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.views.generic import TemplateView
from django.conf.urls import patterns, url

from .views import RegisterView, VerifyMobileView

urlpatterns = patterns(
    '',
    url(r'^$', RegisterView.as_view(), name='rest_register'),
    url(r'^verify_mobile/$', VerifyMobileView.as_view(), name='rest_verify_mobile'),
)
