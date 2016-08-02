# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins, viewsets

from restful.contrib.consumer.models import Feedback
from restful.contrib.consumer.serializers import FeedbackSerializer


class FeedbackViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    意见反馈接口

    只接受`post`请求.
    '''
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # allowed_methods = ('POST', 'OPTIONS', 'HEAD')
