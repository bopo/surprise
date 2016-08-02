# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from restful.models.shared import Shared


class QRCodeSerializer(serializers.ModelSerializer):
    qrcode = serializers.URLField()


class SharedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shared
        fields = ('platform', 'channels', 'model', 'open_iid', 'title')
