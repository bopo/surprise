# -*- coding: utf-8 -*-
from __future__ import unicode_literals

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'yourgmailaccount@gmail.com'
EMAIL_HOST_PASSWORD = 'yourgmailpassword'
