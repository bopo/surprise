# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import filters, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from restful.models.article import Article, ArticleCategory, ArticleComment
from restful.serializers.article import (
    ArticleCategorySerializer, ArticleCommentSerializer, ArticleSerializer
)
from restful.views import BaseViewSet


class ArticleViewSet(viewsets.ModelViewSet, BaseViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = ('id',)
    search_fields = ('^title',)
    filter_fields = '__all__'

    # @action(methods=['post', 'get'], is_for_list=True, endpoint='comments')
    # def comments(self, request, pk=None):
    #     self.serializer_class = CommentSerializer
    #
    #     if request.method == 'GET':
    #         self.queryset = self.get_object().comment_set.all().order_by('-created')
    #         page = self.paginate_queryset(self.queryset)
    #         if page is not None:
    #             serializer = self.get_serializer(page, many=True, context={'request': request})
    #             return self.get_paginated_response(serializer.data)
    #     elif request.method == 'POST':
    #         self.permission_classes = (IsAuthenticated,)
    #         self.check_permissions(request)
    #
    #         serializer = self.get_serializer(data=request.data)
    #
    #         if serializer.is_valid():
    #             data = serializer.data
    #             data['article'] = self.get_object()
    #             data['owner'] = request.user
    #             serializer.create(data)
    #             return Response({'status': 'comment set'}, status.HTTP_201_CREATED)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleCommentViewSet(viewsets.ModelViewSet):
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer
    filter_fields = ('article', 'owner')

    def list(self, request, article_pk=None):
        queryset = ArticleComment.objects.filter(article=article_pk)
        serializer = ArticleCommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, article_pk=None):
        queryset = ArticleComment.objects.filter(pk=pk, article=article_pk)
        maildrop = get_object_or_404(queryset, pk=pk)
        serializer = ArticleCommentSerializer(maildrop)
        return Response(serializer.data)

    def create(self, request, article_pk=None):
        self.permission_classes = (IsAuthenticated,)
        self.check_permissions(request)

        request.data['owner'] = request.user.pk
        request.data['article'] = article_pk

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ArticleCategoryViewSet(viewsets.ModelViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer

# class TagsViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagsSerializer
