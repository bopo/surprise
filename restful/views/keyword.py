# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from restful.models.keyword import Keyword
from restful.serializers.keyword import KeywordSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    '''
    搜索热词接口

    只读接口, 返回热门搜索热词.
    '''
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    allowed_methods = ('GET', 'OPTIONS', 'HEAD')
