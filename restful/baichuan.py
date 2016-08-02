#  -*- coding: utf-8 -*-
import json
import time
import traceback

import top
import top.api
from django.conf import settings
from django.core.paginator import Paginator

from restful.models.goods import Goods

APPKEY = settings.TOP_APPKEY  # '23255563'
SECRET = settings.TOP_SECRET  # 'f7092fdb96f20625742d577820936b5c'
FIELDS = [field.column for field in Goods._meta.fields]


def get_items(item):
    req = top.api.AtbItemsGetRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.cid = item['cid']
    req.keyword = item['title']
    req.fields = "num_iid,open_iid,title,nick,pic_url,price,commission,commission_rate," \
                 "commission_num,commission_volume,seller_credit_score,item_location,volume,promotion_price"

    try:
        resp = req.getResponse()
        nums = resp.get('atb_items_get_response').get('total_results')
        print '[total_results >>', resp.get('atb_items_get_response').get('total_results'), ']', item['title'],

        if nums > 0:
            for result in resp.get('atb_items_get_response').get('items').get('aitaobao_item'):
                if result['open_iid'] == item['open_iid']:
                    # print u'[√] found goods...done!'
                    print u'√'

                    item.update(result)
        else:
            print u'x'
            item['bad'] = True

    except Exception, e:
        print u'x'
        print 'items', e
        # if page <= 10:
        #     return get_items(item, page + 1)

    return item


def get_detail(items):
    open_iids = [x['open_iid'] for x in items]
    open_ids = dict([(x['open_iid'], x['open_id']) for x in items])

    req = top.api.AtbItemsDetailGetRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.fields = "open_iid,cid,title,item_img,pic_url,promotion_price,price,delist_time"
    req.open_iids = ",".join(open_iids)

    try:
        print ':: >>> get detail ...'
        resp = req.getResponse()
        data = resp['atb_items_detail_get_response']['atb_item_details']['aitaobao_item_detail']
        rows = []

        for i, x in enumerate(data):
            item = x['item']
            item['open_id'] = open_ids[item['open_iid']]
            item['item_img'] = json.dumps(item['item_imgs']['item_img'])

            # 合并数据
            item = get_items(item)
            rows.append(item)

            print item['item_imgs'], item['open_id']

            print "[%d] => " % i, item['title']

        # print rows
        return rows

    except Exception, e:

        for k, v in enumerate(items):
            items[k]['bad'] = True

        print 'detail bad items', e.message
        return items


def convert(num_iids, _detail=False):
    req = top.api.TaeItemsListRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.num_iids = ','.join(num_iids)
    req.fields = "title"

    try:
        resp = req.getResponse()

        if len(resp['tae_items_list_response']['items']) == 0:
            return None

        item = [x for x in resp['tae_items_list_response']['items']['x_item']]
        items = []
        rows = []

        paginator = Paginator(item, 10)

        for p in paginator.page_range:
            page = paginator.page(p)

            # 组合 num_iid
            for x in page.object_list:
                items.append(x)

            if _detail and items:
                rows.extend(get_detail(items=items))
                print '[-] sleep 10s ....'
                time.sleep(10)

            items = []
        return rows
    except Exception, e:
        traceback.print_exc()
        print 'covert', e.message
        return []
