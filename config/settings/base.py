# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

import environ

"""
Django settings for life project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
ROOT_DIR = environ.Path(__file__) - 3
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# APPS_DIR = ROOT_DIR.path('apps')

env = environ.Env()
environ.Env.read_env()

FIXTURE_DIRS = (
    ROOT_DIR + '/database/fixtures',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
SECRET_KEY = env('SECRET_KEY', default='s4lk7ni)@9n0+4a!2_$vss8hqks_0#f_ia%i8k!djc87y$@0x5')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", True)

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'restful.middleware.DisableCSRFCheck',
    # 'sslify.middleware.SSLifyMiddleware',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

SITE_ID = 1
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            ],
        },
    },
]

# TEMPLATES = [
#     {
#         # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
#         # 'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
#             'debug': DEBUG,
#             # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
#             # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
#             'loaders': [
#                 'django.template.loaders.filesystem.Loader',
#                 'django.template.loaders.app_directories.Loader',
#             ],
#             # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.template.context_processors.i18n',
#                 'django.template.context_processors.media',
#                 'django.template.context_processors.static',
#                 'django.template.context_processors.tz',
#                 'django.contrib.messages.context_processors.messages',
#                 # Your stuff: custom template context processors go here
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'config.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

# USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'assets', 'static')
THUMB_ROOT = os.path.join(BASE_DIR, '..', 'assets', 'media', 'thumb')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'assets', 'media')

DEFAULT_CHARSET = 'utf-8'

FIXTURE_DIRS = (str(ROOT_DIR.path('fixtures')),)

try:
    from .apps import *
    from .auth import *
    from .rest import *
    from .suit import *

    from .static import *
    from .celery import *

    from .cache import *
    from .thumb import *
    # from .sentry import *
    from .scraper import *

except ImportError, e:
    raise e
