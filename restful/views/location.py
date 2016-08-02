# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from restful.models.location import Location
from restful.serializers.location import LocationSerializer


class LocationViewSet(mixins.CreateModelMixin, GenericViewSet):
    '''
    位置信息

    接受手机端发送来的位置信息, POST时候只需字段:
        - imei: 设备号码
        - address: 详细地址
        - coordinate: 位置坐标,格式为 x,y 形式.(x 经度，y 纬度)
    '''
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
