# -*- coding: utf-8 -*-
import hashlib
import json
import os
import time
import urllib

import requests

from restful.models.goods import Preselection

HEADERS = {
    'Host': 'api.nanyibang.com',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'HKM_SESSION_ID=u02pttq18p0hht3dio9ntteb81',
    'Connection': 'keep-alive',
    'x-ios': '9.3.2',
    'Accept': '*/*',
    'User-Agent': 'nanyibang/2.2.3 (iPhone; iOS 9.3.2; Scale/3.00)',
    'Accept-Language': 'zh-Hans-CN;q=1',
    'x-nanyibang': '2.2.3',
    'x-content': '0227da8226d34eb1bf55d0469e5385c6_5b41f9bde7205b0d6db4a1f2886ebaaf',
}

FIELDS = [field.column for field in Preselection._meta.fields]


def md5(src):
    m2 = hashlib.md5()
    m2.update(src)
    return m2.hexdigest()


def cache_get(key):
    if not os.path.isdir('runtime/cache/' + key):
        return None

    return open('runtime/cache/' + key).read()


def cache_set(key, val=None):
    open('runtime/cache/' + key, 'w').write(json.dumps(val))


def taobao_search(keyword, num_iid):
    keyword = keyword.strip()

    key = md5(keyword + num_iid)
    res = cache_get(key)

    if res:
        return res

    data = {
        'q': keyword,
        'sst': 1,
        'n': 20,
        'buying': 'buyitnow',
        'm': 'api4h5',
        'abtest': 27,
        'wlsort': 27,
        'page': 1,
    }

    # time.sleep(1)

    url = 'http://s.m.taobao.com/search?' + urllib.urlencode(data)

    try:
        req = requests.get(url=url)
        res = req.json()
    except Exception, e:
        print req.content
        print '[!!] time.sleep(3)'
        time.sleep(3)
        return taobao_search(keyword, num_iid)

    for x in res.get('listItem'):
        if num_iid == x['item_id'][1:-3]:
            cache_set(key, x['item_id'])
            return x['item_id']

    return None


def save2db(data):
    if 'id' in data.keys():
        del data['id']

    data['title'] = data['title'].strip()
    model, status = Preselection.objects.get_or_create(num_iid=data.get('num_iid'), source='nanyibang')

    if status:
        for field in FIELDS:
            if data.get(field):
                print field, data.get(field)
                setattr(model, field, data[field])

        model.save()

        print u'[√]', data['title'], data['num_iid']
    else:
        print u'[x]', data['title'], data['num_iid'], data['category'], data['subcategory']

    return True


def item_detail(_id):
    url = 'http://api.nanyibang.com/items?age=29&ios_version=9.3.2&item_id=%s&version=2.2.3' % _id
    req = requests.get(url, headers=HEADERS)
    res = req.json().get('data')

    res['num_iid'] = taobao_search(res['title'], res['num_iid'])

    return res


def categories():
    url = 'http://api.nanyibang.com/select-condition?age=25&system_name=android&versionCode=211'
    req = requests.get(url, headers=HEADERS)

    for cat in req.json().get('data'):
        for sub in cat.get('categories'):
            subcategories(sub, cat)


def subcategories(sub, cat):
    print sub.get('name'), sub.get('cate_id'), cat['classID'], cat['name']
    url = 'http://api.nanyibang.com/single-product?age=29&cate_id=%s&ios_version=9.3.2&page=1&selectType=default&version=2.2.3' % sub.get(
        'cate_id')

    req = requests.get(url=url, headers=HEADERS)
    res = req.json()

    for item in res.get('data'):
        data = item_detail(item['_id'])

        if not data.get('num_iid'):
            continue

        data['source'] = 'nanyibang'

        data['category'] = cat['name']
        data['category_id'] = cat['classID']

        data['subcategory'] = sub['name']
        data['subcategory_id'] = sub['cate_id']

        save2db(data)


# http://api.liwushuo.com/v2/item_categories/tree
#
# http://api.liwushuo.com/v2/item_subcategories/<cid>/items?limit=20&offset=0
#
#
# http://api.nanyibang.com/select-condition?age=25&system_name=android&versionCode=211
#
# http://api.nanyibang.com/tuijian-product?age=29&cateId=<cid>&page=1&system_name=android&versionCode=211
# http://s.m.taobao.com/search\?q\=keywor\&search=%E6%8F%90%E4%BA%A4\&tab\=all\&sst\=1\&n\=20\&buying\=buyitnow\&m\=api4h5\&abtest\=20\&wlsort\=20\&page\=1

def run():
    categories()
