# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import re
import urllib

from django.conf import settings
from django.core.cache import cache
from rest_framework import viewsets, status, filters
# from rest_framework.permissions import IsAuthenticated
from django.contrib.sites.models import Site
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_extensions.decorators import link

from ..models.goods import Collect, GoodsCategory, Preselection
from ..serializers.goods import CollectSerializer, PreselectionSerializer


class CollectViewSet(viewsets.GenericViewSet):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer

    # permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        # key = request.data.get('syn_key')

        # if not key:
        #     return 'key error!'
        # gc = GoodsCategory.objects.filter(parent_id__isnull=True)

        data = cache.get('CollectList')

        if not data:
            data = {
                "status": "success",
                "domain": Site.objects.get(pk=settings.SITE_ID).domain,
                "tae": 0,
                'data':
                    {
                        'channel': [
                            {
                                'name': '',
                                'fid': '',
                                'sub': [],
                            }
                        ]
                    }
            }

            parents = GoodsCategory.objects.filter(parent_id__isnull=True)
            data['data']['channel'] = self.get_channels(parents)
            cache.set('CollectList', data, 3600 * 24 * 7)

        return Response(data)

    def get_channels(self, parents):
        channel_list = []

        for parent in parents:
            channel = {'name': parent.name, 'fid': parent.pk, 'sub': []}
            childrens = parent.get_children()

            if len(childrens) > 0:
                for children in childrens:
                    subcats = {'name': children.name, 'fid': children.pk, 'sub': []}
                    subchild = children.get_children()

                    if len(subchild) > 0:
                        subcats['sub'] = self.get_channels(subchild)

                    channel['sub'].append(subcats)

            channel_list.append(channel)

        return channel_list

    def create(self, request, *args, **kwargs):
        try:
            length = request.data.get('len', 0)
            data = request.data.get('data')
            data = urllib.unquote(str(data))
            data = json.loads(data)
            nums = 0

            open('data.json', 'w').write(json.dumps(data))

            if len(data) != int(length):
                return Response('len error!', status=status.HTTP_403_FORBIDDEN)

            fields = ('commission', 'from_name', 'sid', 'title', 'nick', 'cid', 'num', 'nick')

            for k, v in data.items():
                print k, v['title']
                collect, _status = Collect.objects.get_or_create(num_iid=k)

                if _status:
                    for field in fields:
                        if v.get(field):
                            setattr(collect, field, v.get(field))
                        else:
                            print 'no %s.' % field

                    if v.get('yh_price', None):
                        collect.promotion_price = v.get('yh_price')
                    else:
                        print 'no yh_price'

                    if re.findall(r'\d+\.\d{2}', v['price']):
                        collect.price = re.findall(r'\d+\.\d{2}', v['price'])[0]
                    else:
                        print 'no price'

                    if v.get('picurl'):
                        collect.pic_url = v.get('picurl')
                    else:
                        print 'no picurl'

                    if v.get('shop_type'):
                        collect.shop_type = 'B' if str(v.get('shop_type')) == '1' else 'C'
                    else:
                        print 'no shop_type'

                    if v.get('fid'):
                        collect.category_id = v.get('fid')
                    else:
                        print 'no fid'

                    if v.get('images', None):
                        collect.item_img = json.dumps(v.get('images'))
                    else:
                        print 'no images'

                    collect.save()

                    nums += 1
                    print v['title']
                else:
                    print 'no', v['title']
        except Exception, e:
            return Response(e, status=status.HTTP_403_FORBIDDEN)

        data = {
            'status': "success",
            'domain': Site.objects.get(pk=settings.SITE_ID).domain,
            'msg': "发布成功%d条单品" % nums,
            'len': nums,
            'tae': 0,
        }

        return Response(data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    # max_page_size = 1000


class PreselectionViewSet(viewsets.ModelViewSet):
    queryset = Preselection.objects.all()
    serializer_class = PreselectionSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('source', 'subcategory_id', 'category_id')

    @link(is_for_list=True)
    def items(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset().filter(source=pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
