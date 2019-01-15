# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from restful.models.rules import Rules
from restful.serializers.rules import RulesSerializer


class RulesViewSet(viewsets.ModelViewSet):
    '''
    这个接口是用来返回淘口令规则.
    '''
    queryset = Rules.objects.all()
    allowed_methods = ('GET', 'OPTIONS', 'HEAD')
    serializer_class = RulesSerializer
    permission_classes = (IsAuthenticated,)
