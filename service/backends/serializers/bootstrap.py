# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from restful.models.bootstrap import Channel, Installation, Picture, Version


class InstallationSerializer(serializers.ModelSerializer):
    # channel = serializers.StringRelatedField()

    # @staticmethod
    # def setup_eager_loading(queryset):
    #     queryset = queryset.select_related('channel')
    #     return queryset

    class Meta:
        model = Installation
        fields = ('badge', 'timeZone', 'deviceToken', 'installationId', 'deviceType', 'channel', 'created')


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        # fields = ('photo',)


class VersionSerializer(serializers.ModelSerializer):
    # channel = serializers.StringRelatedField()

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        # select_related for "to-one" relationships
        queryset = queryset.select_related('channel')

        # prefetch_related for "to-many" relationships
        # queryset = queryset.prefetch_related('channel',)

        # Prefetch for subsets of relationships
        # queryset = queryset.prefetch_related(
        #     Prefetch('unaffiliated_attendees',
        #         queryset=Attendee.objects.filter(organization__isnull=True))
        # )

        return queryset

    class Meta:
        model = Version
        fields = ('platform', 'install', 'version', 'sha1sum', 'channel')
        # depth = 1


class ChannelSerializer(serializers.ModelSerializer):
    versions = VersionSerializer(many=True)

    class Meta:
        model = Channel
        fields = ('name',)
