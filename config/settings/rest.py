# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import ISO_8601

from .base import INSTALLED_APPS

INSTALLED_APPS += (
    'rest_framework',
    'rest_framework_word_filter',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'drf_multiple_model',
    'django_filters',
    'corsheaders',
)

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'restful.exception.custom_exception_handler',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_msgpack.renderers.MessagePackRenderer',
        # 'rest_framework_xml.renderers.XMLRenderer',
        # 'rest_framework_yaml.renderers.YAMLRenderer',
    ),
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    #     'rest_framework_xml.parsers.XMLParser',
    #     'rest_framework_msgpack.parsers.MessagePackParser',
    #     'rest_framework_yaml.parsers.YAMLParser',
    # ),
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '100/day',
    #     'user': '1000/day'
    # },
    'PAGE_SIZE': 20,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',

}

REST_AUTH_SERIALIZERS = {
    # 'LOGIN_SERIALIZER': 'path.to.custom.LoginSerializer',
    # 'TOKEN_SERIALIZER': 'path.to.custom.TokenSerializer',
    'USER_DETAILS_SERIALIZER': 'restful.contrib.consumer.serializers.AccountDetailsSerializer',
}

REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_USE_CACHE': 'default'
}

# from rest_framework.versioning import URLPathVersioning
CORS_ORIGIN_ALLOW_ALL = True

ACCOUNT_EMAIL_VERIFICATION = None
OLD_PASSWORD_FIELD_ENABLED = True
