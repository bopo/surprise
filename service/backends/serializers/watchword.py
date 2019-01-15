# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from restful.models.watchword import Watchword


class WatchwordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchword
        fields = ('url', 'watchword', 'sort')
