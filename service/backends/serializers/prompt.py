# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from restful.models.prompt import Prompt, SharePrompt


class SharePromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePrompt
        fields = ('content',)


class PromptSerializer(serializers.ModelSerializer):
    # switchs = serializers.CharField(source='switchs')

    class Meta:
        model = Prompt
        fields = ('switchs', 'content', 'forward', 'first_msg', 'second_msg', 'third_msg')
