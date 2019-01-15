# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, mixins
from rest_framework.filters import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from restful.models.bootstrap import Picture, Version
from restful.models.reward import First
from restful.serializers.bootstrap import (
    Installation, InstallationSerializer,
    PictureSerializer, VersionSerializer)

# class CreateModelMixin(object):
#     """
#     Create a model instance.
#     """
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#     def get_success_headers(self, data):
#         try:
#             return {'Location': data[api_settings.URL_FIELD_NAME]}
#         except (TypeError, KeyError):
#             return {}
from restful.serializers.start import FirstSerializer


class InstallationViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAdminUser,)


class PictureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Picture.objects.all().order_by('ordering')
    serializer_class = PictureSerializer
    permission_classes = (AllowAny,)


class VersionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Version.objects.all().order_by('-version')
    serializer_class = VersionSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (AllowAny,)
    filter_fields = ('channel', 'platform')



