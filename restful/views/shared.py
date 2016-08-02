# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from requests import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_extensions.decorators import action

from restful.models.shared import Shared
from restful.serializers.shared import SharedSerializer


class SharedViewSet(viewsets.ModelViewSet):
    '''
    分享回调接口

    - 该接口接收分享成功后的回调数据.
    - POST 方法接受回调数据,存储数据库.
    - GET 方法返回当前用户的分享记录.

    字段待定,需要前端开发的给我...
    '''
    queryset = Shared.objects.all()
    serializer_class = SharedSerializer
    permission_classes = (IsAuthenticated,)

    @action(is_for_list=False)
    def qrcode(self, request, pk=None):
        return Response(['password changed'])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_object(self):
        return self.request.user.shared_set.all()

    def get_queryset(self):
        return self.request.user.shared_set.all()

# class QRCodeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     '''
#     分享回调接口
#
#     - 该接口接收分享成功后的回调数据.
#     - POST 方法接受回调数据,存储数据库.
#     - GET 方法返回当前用户的分享记录.
#
#     字段待定,需要前端开发的给我...
#     '''
#     serializer_class = QRCodeSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#
#         page = self.paginate_queryset(queryset)
#         user = request.user.get()
#
#         if user.qrcode is None:
#             user.qrcode = ''
#
#         user.save()
#
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
