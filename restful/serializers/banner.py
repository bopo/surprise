# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from restful.models.banner import Banner


class BannerSerializer(serializers.ModelSerializer):
    # thumbnail = serializers.ImageField(source='cover.thumbnail')

    class Meta:
        model = Banner
        # fields = ('summary', 'click', 'cover')
