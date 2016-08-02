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
    del data['id']

    print data['purchase_id'], data['title']
    model, status = Preselection.objects.get_or_create(num_iid=data.get('num_iid'), title=data['title'])

    for field in FIELDS:
        if data.get(field):
            print field, data.get(field)
            setattr(model, field, data[field])

    model.save()

    print u'[√]', data['title']
    return True


def categories():
    url = 'http://api.liwushuo.com/v2/item_categories/tree'
    req = requests.get(url, headers=HEADERS)

    for cat in req.json().get('data').get('categories'):
        for sub in cat.get('subcategories'):
            subcategories(sub, cat)


def subcategories(sub, cat):
    url = 'http://api.liwushuo.com/v2/item_subcategories/%s/items?limit=20&offset=0' % sub.get('id')
    req = requests.get(url, headers=HEADERS)
    txt = req.json()

    items = txt.get('data').get('items')

    for item in items:
        data = item

        if not data['purchase_id']:
            continue

        data['pic_url'] = data['cover_image_url'].replace('w720', 'w180')
        data['num_iid'] = data['purchase_id']
        data['title'] = data['name']
        data['source'] = 'liwushuo'
        data['category'] = cat['name']
        data['subcategory'] = sub['name']
        data['subcategory_id'] = data['subcategory_id']
        data['category_id'] = data['category_id']

        save2db(data)


# http://api.liwushuo.com/v2/item_categories/tree
#
# http://api.liwushuo.com/v2/item_subcategories/<cid>/items?limit=20&offset=0
#
#
# http://api.nanyibang.com/select-condition?age=25&system_name=android&versionCode=211
#
# http://api.nanyibang.com/tuijian-product?age=29&cateId=<cid>&page=1&system_name=android&versionCode=211

def run():
    categories()
