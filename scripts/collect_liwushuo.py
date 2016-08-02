# -*- coding: utf-8 -*-
import requests

from restful.models.goods import Preselection

HEADERS = {
    'X-OS': 'iOS 9.3.2',
    'X-NETCLS': 'WiFi',
    'X-UDID': '17761F4A-CA62-4059-B9E8-B26EC46F798E',
    'X-CHAN': 'App Store',
    'Accept-Language': 'zh-Hans-CN;q=1',
    'X-VER': '3.0.0',
    'X-DEV': 'iPhone8,2',
    'X-APP': 'com.liwushuo.gifttalk',
    'User-Agent': 'GiftTalk/731 Mozilla (iPhone8,2; OS 9.3.2 like Mac OS X) Mobile',
    'Connection': 'keep-alive',
    'X-BUILD': '731',
    'Cookie': 'session=9d9d11a9-dd8f-4d43-b2f3-06cd6187565e',
    'X-Tingyun-Id': '4u9dmihYv_A;c=2;r=60845535',
}

FIELDS = [field.column for field in Preselection._meta.fields]


def save2db(data):
    print data['purchase_id'], data['title']
    model, status = Preselection.objects.get_or_create(num_iid=data.get('num_iid'), title=data['title'])

    for field in FIELDS:
        if data.get(field):
            print field, data.get(field)
            setattr(model, field, data[field])

    model.save()

    print u'[√]', data['title']
    return True


def items():
    url = 'http://api.liwushuo.com/v2/item_categories/tree'
    req = requests.get(url, headers=HEADERS)
    cat = req.json()

    for pid in cat:
        pid.get('name')
        sub = pid.get('subcategories')


def run():
    url = 'http://api.liwushuo.com/v2/items?gender=1&generation=1&limit=100&offset=0'
    r = requests.get(url, headers=HEADERS)
    i = r.json()
    items = i.get('data').get('items')

    for item in items:
        data = item.get('data')
        # 写入数据库函数

        if not data['purchase_id']:
            continue

        data['pic_url'] = data['cover_image_url'].replace('w720', 'w180')
        data['num_iid'] = data['purchase_id']
        data['title'] = data['name']
        data['source'] = '123'
        del data['id']
        save2db(data)

    items()
