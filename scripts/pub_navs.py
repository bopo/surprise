#  -*- coding: utf-8 -*-
import json
import os
import sys
import time
import urllib
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), 'verdors'))

import top
import top.api
import requests

from restful.models.goods import Goods, TBKCategory
from django.conf import settings

APPKEY = settings.TOP_APPKEY  # '23255563'
SECRET = settings.TOP_SECRET  # 'f7092fdb96f20625742d577820936b5c'
FIELDS = [field.column for field in Goods._meta.fields]

BASE_URL = 'http://pub.alimama.com/items/channel/{channel}.json?'

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
    print data.get('promotion_price'), did

    # if not status:
    # goods.category_recommend = did

    goods.category_id = did
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

            print "[%d] => " % i, item['title']

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

                ids = []
                time.sleep(2)
    except Exception, e:
        print(e.message)


def build_query(page=1, catIds=None, channel='nzjh'):
    data = {
        # 'channel': channel,
        # '_tb_token_': 'test',
        # 'pvid': '21_118.247.89.212_362_1460981902455',
        # 'perPageSize': '50',
        # 'toPage': str(page),
        # 'shopTag': '',
        # 't': '1460981991072',
        # 'catIds': catIds,
        # 'level': 1,
    }

    if catIds:
        data['catIds'] = catIds
        data['level'] = 1

    return BASE_URL.replace('{channel}', channel) + urllib.urlencode(data)


channelss = (
    '女装尖货 nzjh',
    '流行男装 ifs 50344007',
    '母婴热推 muying',
    '亲宝贝 qbb',
    'ifashion ifs',
    '汇吃 hch',
    '潮电街 cdj',
    '极有家 jyj',
    '酷动城 kdc',
    'DIY diy',
    '超值9块9 9k9',
    '特价好货 tehui',
    '20元封顶 20k',
    '高佣活动 qqhd',
)

k = 1
channels = []

for c in channelss:
    c = c.split(' ')

    if len(c) >= 3:
        catid = c[2]
    else:
        catid = None

    channels.append({'name': c[0], 'slug': c[1], 'id': k, 'catid': catid})
    k += 1


def navs(channels):
    '''
    name: "工作制服/校服",
    id: 50103026,
    type: "category",
    level: 1,
    count: "350",
    flag: "channel_fcat",
    subIds: null
    '''
    for channel in channels:
        url = build_query(channel=channel['slug'], catIds=channel['catid'])
        print url
        req = requests.get(url=url)
        rep = json.loads(req.content)

        try:
            parent, status = TBKCategory.objects.get_or_create(name=channel['name'], channel=channel['slug'])
        except Exception, e:
            print channel
            raise e

        for x in rep['data']['navigator']:

            if x.get('subIds'):
                for sub in x.get('subIds'):
                    print channel.get('name'), sub.get('name'), sub.get('id')

                    # if sub.get('id') < 20:
                    #     continue

                    tt, ss = TBKCategory.objects.get_or_create(name=sub.get('name'), cid=sub.get('id'), parent=parent)

                    # t.subIds = x.get('subIds')
                    tt.level = sub.get('level')
                    tt.count = sub.get('count')
                    tt.type = sub.get('type')
                    tt.flag = sub.get('flag')
                    tt.channel = channel.get('slug')
                    # tt.parent = parent

                    tt.save()
            else:
                print channel.get('name'), x.get('name'), x.get('id')
                # if x.get('id') < 20:
                #     continue
                t, s = TBKCategory.objects.get_or_create(name=x.get('name'), cid=x.get('id'), parent=parent)

                # t.subIds = x.get('subIds')
                t.level = x.get('level')
                t.count = x.get('count')
                t.type = x.get('type')
                t.flag = x.get('flag')
                t.channel = channel.get('slug')
                # t.parent = parent
                t.save()

                # raise e


def main(channel, pages, cats, syncdb):
    pages = pages
    cats = cats
    iids = []

    for page in xrange(1, int(pages) + 1):
        req = requests.get(build_query(page, catIds=None, channel=channel))
        rep = json.loads(req.content)
        ids = [str(x['auctionId']) for x in rep['data']['pageList']]
        ids = {}.fromkeys(ids).keys()
        ids = ",".join(ids)

        print ' -- page=%d' % page

        iids.append(convert(ids, cats))

        print iids


def run():
    navs(channels=channels)
