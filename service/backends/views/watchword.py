 # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import json
import re

import requests
import top
import top.api
from django.conf import settings
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import GenericViewSet

from restful.models.watchword import Watchword
from restful.serializers.watchword import WatchwordSerializer

FIELDS = "open_iid,open_iid,title,pic_url,price,promotion_price,item_location,nick"


def detail(open_iids):
    req = top.api.AtbItemsDetailGetRequest()
    req.set_app_info(top.appinfo(settings.TOP_APPKEY, settings.TOP_SECRET))
    req.fields = "open_iid,cid,title,item_imgs,pic_url,promotion_price,price"
    req.open_iids = open_iids

    # print open_iids

    try:
        resp = req.getResponse()
        # for x in resp['atb_items_detail_get_response']['atb_item_details']['aitaobao_item_detail']:
        # print x.get('item').get('title'), x.get('item').get('price')
        # print len(resp['atb_items_detail_get_response']['atb_item_details']['aitaobao_item_detail'])
        data = resp['atb_items_detail_get_response']['atb_item_details']['aitaobao_item_detail'][0]['item']
        #
        # for x in data:
        #     for field in FIELDS:
        #         if hasattr(x, field):
        #             print x[field]

        return data

    except Exception, e:
        raise e


def convert(iids):
    req = top.api.TaeItemsListRequest()
    req.set_app_info(top.appinfo(settings.TOP_APPKEY, settings.TOP_SECRET))
    req.fields = "title"
    req.num_iids = iids

    try:
        resp = req.getResponse()
        # open_iids = ",".join([x['open_iid'] for x in resp['tae_items_list_response']['items']['x_item']])
        open_iids = [x['open_iid'] for x in resp['tae_items_list_response']['items']['x_item']]
        print open_iids
        return open_iids
    except Exception, e:
        print(e)


def items(keyword, page_size, sort='price_asc'):
    inf = top.appinfo(settings.TOP_APPKEY, settings.TOP_SECRET)
    req = top.api.AtbItemsGetRequest()

    req.set_app_info(inf)

    req.fields = FIELDS
    req.keyword = keyword.decode('utf8')
    req.page_size = page_size
    req.sort = sort

    try:
        resp = req.getResponse()
        if int(resp.get('atb_items_get_response').get('total_results')) > 0:
            return resp.get('atb_items_get_response').get('items').get('aitaobao_item')
    except Exception, e:
        raise e


def watchword(str=None):
    if str is None:
        return None

    m = re.findall(r'http://\S+', str)
    key = None
    biz = None
    item = {}

    if m:
        print m
        req = requests.get(m[0])
        txt = re.findall(r'var pageData =(.*?);', req.content)

        if txt:
            items = json.loads(txt[0])
            # item['num_id'] = items['tmallShareExt']['itemId']
            item['title'] = items.get('content')
            item['pic_url'] = 'http:' + items.get('backgroundImg')['m']
            item['price'] = items.get('itemPrice')
            item['promotion_price'] = items.get('itemPrice')
            item['open_iid'] = convert(items['tmallShareExt']['itemId'])[0]
            print item
            return item['title'], [item]

        url = re.findall(r'var url = \'([^"]+)\'', req.content)

        if not url:
            url = re.findall(r'"url":"([^"]+)"', req.content)

        url = url[0]

        # if 'ewqcxz.com' in m[0]:
        #     url = re.findall(r'var url = \'([^"]+)\'', req.content)[0]
        # if 'laiwang.com' in m[0]:
        #     url = re.findall(r'"url":"([^"]+)"', req.content)[0]
        # elif 'mashort.cn' in m[0]:
        #     url = re.findall(r'var url = \'([^"]+)\'', req.content)[0]

        if url:
            print url
            req = requests.get(url)
            key = re.findall('<title>(.*?)</', req.content)[0].split('-')[0].strip()
            key = key.decode('gbk')

            watch = Watchword(watchword=key)
            watch.save()

    if not key:
        m = re.findall(r'【(.*)】', str)

        if m:
            key = m[0].strip()

    return key, biz


class WatchwordViewSet(GenericViewSet):
    '''
    淘口令提交接口

    该接口只接收post方法, 提交后会返回对应的商品数据.
    '''
    queryset = Watchword.objects.all()
    serializer_class = WatchwordSerializer
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def create(self, request, *args, **kwargs):
        word = request.data.get('watchword')
        sort = request.data.get('sort')
        word, item = watchword(word)

        if word is None:
            data = {'errors': {'code': '400', 'msgs': '您复制的内容不是一个正确的淘口令或瞄口令.'}}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        if not item:
            item = items(word, 50, sort)

        if item:
            for k, v in enumerate(item):
                item[k]['thumb'] = '%s_800x800.jpg' % v.get('pic_url')
                item[k]['detail_url'] = reverse('v1.0:goods-detail', request=request, args=[v.get('open_iid')])
                cache.set(v.get('open_iid'), item[k], 60)
        else:
            item = []

        data = {'results': item}
        return Response(data, status=status.HTTP_201_CREATED)
