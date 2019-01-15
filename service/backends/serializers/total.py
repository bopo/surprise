# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from restful.models.total import Total, Trend


class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = ('first', 'second', 'third', 'exchange', 'number')


class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ('exchange', 'number')
