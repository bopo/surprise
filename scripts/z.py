#  -*- coding: utf-8 -*-
import os
import urllib

import django
from django.core.paginator import Paginator

import scripts.taobao.top.api
import top

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

if django.VERSION >= (1, 7):
    django.setup()

from restful.models.goods import GoodsItems, Goods

APPKEY = '23255563'
SECRET = 'f7092fdb96f20625742d577820936b5c'
FIELDS = [field.column for field in Goods._meta.fields]

BASE_URL = 'http://pub.alimama.com/items/channel/nzjh.json?'


def detail(open_iids):
    req = top.api.AtbItemsDetailGetRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.fields = "open_iid,cid,title,item_imgs,pic_url,promotion_price,price"
    req.open_iids = open_iids

    # print open_iids

    try:
        resp = req.getResponse()
        for x in resp['atb_items_detail_get_response']['atb_item_details']['aitaobao_item_detail']:
            print x.get('item').get('title'), x.get('item').get('price')
            # print len(resp['atb_items_detail_get_response']['atb_item_details']['aitaobao_item_detail'])
            # data = resp['atb_items_detail_get_response']['atb_item_details']['aitaobao_item_detail'][0]['item']
            #
            # for x in data:
            #     for field in FIELDS:
            #         if hasattr(x, field):
            #             print x[field]

            # return data

    except Exception, e:
        raise e


def convert(iids):
    req = top.api.TaeItemsListRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.fields = "title"
    req.num_iids = ",".join(iids)

    try:
        resp = req.getResponse()
        open_iids = ",".join([x['open_iid'] for x in resp['tae_items_list_response']['items']['x_item']])
        detail(open_iids)
    except Exception, e:
        print(e)


def build_query(page=1, cids=None):
    data = {
        'channel': 'nzjh',
        '_tb_token_': 'oaKCw9VDQRp',
        'pvid': '21_118.247.89.212_362_1460981902455',
        'perPageSize': '50',
        'toPage': str(page),
        'shopTag': '',
        't': '1460981991072'
    }

    if cids is not None:
        data['level'] = 1
        data['catIds'] = str(cids)

    return BASE_URL + urllib.urlencode(data)


def main():
    rows = GoodsItems.objects.values('auctionId')
    page = Paginator(rows, 50)
    data = []

    for p in page.page_range:
        ids = [str(v['auctionId']) for v in page.page(p).object_list]
        print len(page.page(p).object_list)
        # print ids
        detail = convert(ids)
        # print detail
        # data.append(detail)
        break

    # print data
    return data


if __name__ == '__main__':
    # page = sys.argv[1] if len(sys.argv) > 1 else 1
    main()
    # print build_query(10, 1200)
