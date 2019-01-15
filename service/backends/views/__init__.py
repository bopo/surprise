# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIRootView(APIView):
    def get(self, request):
        data = {
            'v1-url': reverse('v1', request=request)
        }
        return Response(data)


# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.decorators import action

from restful.contrib.consumer.models import Like, Favorite
from restful.   contrib.consumer.serializers import LikeSerializer, FavoriteSerializer


class BaseViewSet(viewsets.GenericViewSet):
    @action(methods=['post'], endpoint='favorite')
    def favorite(self, request, pk=None):
        self.serializer_class = FavoriteSerializer
        self.permission_classes = (IsAuthenticated,)
        self.check_permissions(request)

        fav = Favorite(content_object=self.get_object(), owner=request.user)
        fav.validate_unique()
        fav.save()

        return Response({'detail': 'favorite seted'}, status.HTTP_201_CREATED)

    @action(methods=['post'], endpoint='like')
    def like(self, request, pk=None):
        self.serializer_class = LikeSerializer
        self.permission_classes = (IsAuthenticated,)
        self.check_permissions(request)

        obj = Like(content_object=self.get_object(), owner=request.user)
        obj.validate_unique()
        obj.save()

        return Response({'detail': 'like seted'}, status.HTTP_201_CREATED)
