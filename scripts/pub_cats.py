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

from restful.models.goods import Goods, GoodsCategory as Category, GoodsCategory
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


def json2db(data, did='29', recommend=None):
    goods, status = Goods.objects.get_or_create(open_iid=data['open_iid'])
    print data.get('promotion_price'), did

    # if not status:
    if recommend:
        goods.category_recommend = recommend

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


def items(item, did, recommend):
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
                return json2db(result, did, recommend)

        print '[!] no found item...'
        print item['cid'], item['title']

    except Exception, e:
        print e


def detail(open_iids, did, recommend):
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
            rows.append(items(item, did, recommend))

            print "[%d] => " % i, item['title']

        return data

    except Exception, e:
        print e


def convert(num_iids, did, recommend):
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
                    detail(ids, did, recommend)

                ids = []
                time.sleep(2)
    except Exception, e:
        print(e.message)


def build_query(page=1, catIds=None, channel='nzjh'):
    data = {
        'channel': channel,
        # '_tb_token_': 'test',
        # 'pvid': '21_118.247.89.212_362_1460981902455',
        # 'perPageSize': '50',
        # 'toPage': str(page),
        # 'shopTag': '',
        # 't': '1460981991072',
        # 'catIds': catIds,
        # 'level': 1,
    }

    if catIds is not None:
        data['catIds'] = catIds
        data['level'] = 1
    print data
    return BASE_URL.replace('{channel}', channel) + urllib.urlencode(data)


channelss = (
    '女人 nzjh 0 2',
    '男人 ifs 50344007 1',
    '潮童 muying 0 90',
    # '亲宝贝 qbb',
    # 'ifashion ifs',
    # '汇吃 hch',
    # '潮电街 cdj',
    # '极有家 jyj',
    # '酷动城 kdc',
    # 'DIY diy',
    # '超值9块9 9k9',
    # '特价好货 tehui',
    # '20元封顶 20k',
    # '高佣活动 qqhd',
)

k = 1
channels = []

for c in channelss:
    c = c.split(' ')

    catid = c[2] if int(c[2]) > 0 else None

    channels.append({'name': c[0], 'slug': c[1], 'id': c[-1], 'catid': catid})
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
    # Category.objects.all().delete()

    for channel in channels:
        url = build_query(channel=channel['slug'], catIds=channel['catid'])
        print url
        req = requests.get(url=url)
        rep = json.loads(req.content)

        try:
            parent = Category.objects.get(pk=channel['id'])
            Category.objects.filter(parent=parent).delete()
        except Exception, e:
            print channel
            raise e

        for x in rep['data']['navigator']:
            if x.get('subIds'):
                for sub in x.get('subIds'):
                    print channel.get('name'), sub.get('name'), sub.get('id')
                    tt, ss = Category.objects.get_or_create(name=sub.get('name'), catids=sub.get('id'), parent=parent)
                    tt.is_active = 1
                    tt.save()
            else:
                print channel.get('name'), x.get('name'), x.get('id')
                t, s = Category.objects.get_or_create(name=x.get('name'), catids=x.get('id'), parent=parent)
                t.is_active = 1
                t.save()


def main():
    iids = []
    # Goods.objects.all().delete()
    GoodsCategory.objects.filter(catids__in=['19254', '19246', '19253', '19257', '19260']).delete()
    pc = GoodsCategory.objects.filter(pk__in=[1, 2, 90])

    for x in pc:
        Goods.objects.filter(category_recommend=x.pk).delete()
        url = build_query(1, catIds=x.catids, channel=x.channel)
        req = requests.get(url=url)
        rep = json.loads(req.content)
        ids = [str(m['auctionId']) for m in rep['data']['pageList']]
        ids = {}.fromkeys(ids).keys()
        ids = ",".join(ids)

        iids.append(convert(ids, x.pk, recommend=x.pk))

        for c in x.get_children():
            Goods.objects.filter(category_id=c.pk).delete()
            catid = c.catids

            if x.catids:
                catid = '%s,%s' % (c.catids, x.catids)

            req = requests.get(build_query(1, catIds=catid, channel=x.channel))
            rep = json.loads(req.content)
            ids = [str(i['auctionId']) for i in rep['data']['pageList']]
            ids = {}.fromkeys(ids).keys()
            ids = ",".join(ids)

            iids.append(convert(ids, c.pk, recommend=None))

            print c.catids, c.name, x.channel


def run():
    main()
    # navs(channels=channels)
