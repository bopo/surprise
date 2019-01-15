# -*- coding: utf-8 -*-
import json
import re
import traceback

import jpush as jpush
import top
from django.conf import settings
from jinja2 import Template

from restful.models.goods import Collect

APPKEY = settings.TOP_APPKEY
SECRET = settings.TOP_SECRET


def response(jsonobj, key):
    obj = jsonobj.get(key)
    suc = False

    if obj:
        success = obj.get('result').get('successful')

        if success is True:
            suc = True

        msg = obj.get('result').get('message')
    else:
        msg = obj.get('error_response').get('sub_msg')

    return [suc, msg]


def send_verify_code(mobile):
    req = top.api.OpenSmsSendvercodeRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.send_ver_code_request = {'mobile': int(mobile)}

    try:
        resp = req.getResponse()
        return response(resp, 'open_sms_sendvercode_response')
    except Exception, e:
        print(e)
        return False


def check_verify_code(mobile, verify):
    req = top.api.OpenSmsCheckvercodeRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.check_ver_code_request = {'mobile': int(mobile), 'ver_code': int(verify)}

    try:
        resp = req.getResponse()
        return response(resp, 'open_sms_checkvercode_response')
    except Exception, e:
        raise e


def get_itmes(keyword, page_size):
    FIELDS = "open_iid,coupon_price,open_iid,title,nick,pic_url,price,commission,commission_rate,commission_num," \
             "commission_volume,seller_credit_score,item_location,volume"
    req = top.api.AtbItemsGetRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))

    req.fields = FIELDS
    req.keyword = keyword.decode('utf8')
    req.page_size = page_size

    try:
        resp = req.getResponse()
        return response(resp, 'atb_items_get_response')
    except Exception, e:
        raise e


def geo2addr(location='39.983424,116.322987'):
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)',
        'Referer': 'http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding',
    }

    url = 'http://api.map.baidu.com/geocoder/v2/?ak=E4805d16520de693a3fe707cdc962045&callback=renderReverse' \
          '&location=%s&output=json&pois=1' % location
    req = requests.get(url, headers=headers)
    txt = req.content
    txt = txt.replace('renderReverse&&renderReverse(', '').replace(')', '')

    return txt


def pushMessage(messages=None, extra=None, *args, **kwargs):
    template = Template(messages)
    messages = template.render(dict(*args, **kwargs))

    push = jpush.JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    push = push.create_push()

    push.notification = jpush.notification(alert=messages, ios=messages, android=messages)
    push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": False}
    push.platform = jpush.platform("ios", "android")
    push.send()


def do_push_msgs(msgs=None, mobile=None, registration_id=None, *args, **kwargs):
    opts = jpush.JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    push = opts.create_push()

    extras = {'mobile': mobile}

    push.notification = jpush.notification(alert=msgs)

    push.options = {"time_to_live": 86400, "apns_production": True, 'extras': extras}

    push.audience = jpush.audience(jpush.registration_id(registration_id)) if registration_id else jpush.all_
    push.platform = jpush.all_

    push.send()


def ItemsGet(keyword, rules, **kwargs):
    FIELDS = "open_iid,open_iid,title,pic_url,price,promotion_price,item_location,nick"
    req = top.api.AtbItemsGetRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))

    column = [field.column for field in rules._meta.fields]

    if rules:
        for field in column:
            if hasattr(rules, field) and field != 'id':
                value = rules.__getattribute__(field)
                if value:
                    setattr(req, field, value)

    # for key in rules:
    #     if hasattr(req, key):
    #         req.__setattr__(key, rules[key])

    for key in kwargs:
        if hasattr(req, key):
            req.__setattr__(key, kwargs[key])

    if req.fields is None:
        req.fields = FIELDS

    req.keyword = keyword.decode('utf8')

    try:
        resp = req.getResponse()
        if int(resp.get('atb_items_get_response').get('total_results')) > 0:
            return resp.get('atb_items_get_response').get('items').get('aitaobao_item')
        else:
            return None
    except Exception, e:
        raise e


def DetailGet(open_iids, *args, **kwargs):
    req = top.api.AtbItemsDetailGetRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))
    req.fields = "open_iid,cid,title,desc,item_img,pic_url,promotion_price,price"
    req.open_iids = open_iids

    try:
        resp = req.getResponse()
        data = resp['atb_items_detail_get_response']['atb_item_details']['aitaobao_item_detail'][0]['item']
        data['item_imgs'] = data['item_imgs']['item_img']
        data['description'] = data['desc']
        return data
    except Exception, e:
        print(e)
        return None


def import2db(data):
    fields = ('commission', 'from_name', 'sid', 'title', 'nick', 'cid', 'num',)

    try:
        collect, _status = Collect.objects.get_or_create(num_iid=data['num_iid'])

        if _status or not collect.category_id:
            v = data

            for field in fields:
                if v.get(field):
                    setattr(collect, field, v.get(field))
                else:
                    print 'no %s.' % field

            if v.get('coupon_price', None):
                collect.promotion_price = v.get('coupon_price')
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

            if v.get('category_id'):
                collect.category_id = v.get('category_id')
            else:
                print 'no category_id'

            if v.get('images', None):
                collect.item_img = json.dumps(v.get('images'))
            else:
                print 'no images'

            collect.save()
            print '[√] ', v['category'], v['title'], 'Saved'
            return True
        else:
            print '[!!]', data['category'], data['title'], 'Already exist.'
            return False
    except Exception:
        traceback.print_exc()
