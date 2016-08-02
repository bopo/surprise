# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from restful.models.rules import Rules


class RulesSerializer(serializers.ModelSerializer):


    class Meta:
        model = Rules
        fields = ('platform', 'content',)
