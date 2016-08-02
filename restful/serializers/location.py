# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from restful.models.location import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'coordinate', 'imei')
