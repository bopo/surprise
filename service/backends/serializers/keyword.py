# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from restful.models.keyword import Keyword


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('keyword', )
