# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import INSTALLED_APPS

INSTALLED_APPS += (
    # 'oauth_provider',
    # 'allauth',
)

ANONYMOUS_USER_ID = -1

AUTH_USER_MODEL = 'consumer.CustomUser'
AUTH_PROFILE_MODULE = 'consumer.Profile'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yourgmailaccount@gmail.com'
EMAIL_HOST_PASSWORD = 'yourgmailpassword'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'restful.contrib.restauth.backends.CustomUserBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = 'mobile'