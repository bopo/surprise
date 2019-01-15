# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from restful.contrib.utils.imports import import_submodules


class DynamicFieldsModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        # select_related for "to-one" relationships
        # queryset = queryset.select_related('creator')

        # prefetch_related for "to-many" relationships
        # queryset = queryset.prefetch_related('attendees', 'attendees__organization')

        # Prefetch for subsets of relationships
        # queryset = queryset.prefetch_related(
        #     Prefetch('unaffiliated_attendees', queryset=Attendee.objects.filter(organization__isnull=True))
        # )
        return queryset


import_submodules(locals(), __name__, __path__)
