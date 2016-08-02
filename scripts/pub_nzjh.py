#  -*- coding: utf-8 -*-
import json
import os
import sys
import time
import urllib
from datetime import datetime

import requests

from scripts.pub_base import navs

sys.path.append(os.path.join(os.path.dirname(__file__), 'verdors'))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

import top
import top.api
#
# if django.VERSION >= (1, 7):
#     django.setup()

from restful.models.goods import Goods
from django.conf import settings

APPKEY = settings.TOP_APPKEY  # '23255563'
SECRET = settings.TOP_SECRET  # 'f7092fdb96f20625742d577820936b5c'
FIELDS = [field.column for field in Goods._meta.fields]

BASE_URL = 'http://pub.alimama.com/items/channel/nzjh.json?'

CATID = 29
pk = 1


def build_data(pk, cid, fields):
    data = {
        "pk": pk,
        "model": "restful.goods",
        "fields": {
            "price": fields.get('price'),
        }
    }

    fields = {}

    for field in FIELDS:
        if data.get(field):
            fields[field] = data[field]

    data = {
        "pk": '{pk}',
        "model": "restful.goods",
        "fields": fields
    }

    return data


def json2db(data, did='29'):
    goods, status = Goods.objects.get_or_create(open_iid=data['open_iid'])
    print data.get('promotion_price')

    if status is False:
        goods.category_recommend = did
        goods.recommend = True

        for field in FIELDS:
            if data.get(field):

                if field == 'delist_time':
                    data[field] = datetime.strptime(data[field], "%Y-%m-%d %H:%M:%S")

                setattr(goods, field, data[field])

        print 'saving...',
        goods.save()
        print 'done!'


def items(item, did):
    req = top.api.AtbItemsGetRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.cid = item['cid']
    req.keyword = item['title'].encode('utf-8')
    req.fields = "open_iid,title,nick,pic_url,price,commission,commission_rate," \
                 "commission_num,commission_volume,seller_credit_score,item_location,volume,promotion_price"

    try:
        resp = req.getResponse()
        print '- get items'
        for result in resp.get('atb_items_get_response').get('items').get('aitaobao_item'):
            if result['open_iid'] == item['open_iid']:
                print 'found goods...done!'
                result.update(item)
                return json2db(result, did)

        print '[!] no found item...'
        print item['cid'], item['title']

    except Exception, e:
        print e


def detail(open_iids, did):
    req = top.api.AtbItemsDetailGetRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.fields = "open_iid,cid,title,desc,item_imgs,pic_url,promotion_price,price,delist_time"
    req.open_iids = ",".join(open_iids)

    try:
        print '- get detail ...'
        resp = req.getResponse()
        data = resp['atb_items_detail_get_response']['atb_item_details']['aitaobao_item_detail']
        rows = []

        for i, x in enumerate(data):
            item = x['item']

            for field in FIELDS:
                if hasattr(item, field):
                    rows[field] = item[field]

            # 合并数据
            rows.append(items(item, did))

            print "[%d] => " % i

        return data

    except Exception, e:
        print e


def convert(num_iids, did):
    req = top.api.TaeItemsListRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.fields = "title"
    req.num_iids = num_iids

    try:
        resp = req.getResponse()
        open_iids = [x['open_iid'] for x in resp['tae_items_list_response']['items']['x_item']]
        ids = []

        for i, x in enumerate(open_iids):
            i += 1

            if x is not None:
                ids.append(x)

            if i % 10 == 0:
                if ids:
                    detail(ids, did)
                print ids
                ids = []
                time.sleep(2)
    except Exception, e:
        print(e.message)


def build_query(page=1, catIds=None):
    data = {
        'channel': 'nzjh',
        '_tb_token_': 'test',
        'pvid': '21_118.247.89.212_362_1460981902455',
        'perPageSize': '50',
        'toPage': str(page),
        'shopTag': '',
        't': '1460981991072',
        # 'catIds': catIds,
        'level': 1,
    }

    return BASE_URL + urllib.urlencode(data)


# @click.command()
# @click.option('--sid', prompt='taobao catid', help='taobao catid.', default=None)
# @click.option('--did', prompt='app catid', help='app catid', default=None)
# @click.option('--pages', prompt='page', help='page num', default=1)
# @click.option('--cats', prompt='cats', help='page num', default=2)

def run():
    navs(channel='nzjh')
    # pages = 2
    # cats = 2
    # iids = []
    #
    # for page in xrange(1, int(pages) + 1):
    #     req = requests.get(build_query(page, catIds=None))
    #     rep = json.loads(req.content)
    #     ids = [str(x['auctionId']) for x in rep['data']['pageList']]
    #     ids = {}.fromkeys(ids).keys()
    #     ids = ",".join(ids)
    #
    #     print ids
    #     print ' -- page=%d' % page
    #
    #     iids.append(convert(ids, cats))
    #
    #     print iids
