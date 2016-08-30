# -*- coding: utf-8 -*-

import requests

from restful.models.goods import PreselectionCategory

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

SOURCE = 'nanyibang'


def run():
    url = 'http://api.nanyibang.com/select-condition?age=25&system_name=android&versionCode=211'
    req = requests.get(url, headers=HEADERS)
    num = 1

    PreselectionCategory.objects.filter(source=SOURCE).delete()

    for cat in req.json().get('data'):
        parent, status = PreselectionCategory.objects.get_or_create(source=SOURCE, name=cat['name'])
        if status is True:
            parent.subcategory_id = cat['classID']
            parent.ordering = num
            parent.save()
            num += 1

        print 'parent:', parent, 'status:', status
        for sub in cat.get('categories'):
            subcat, _status = PreselectionCategory.objects.get_or_create(source=SOURCE, name=sub['name'], parent=parent)
            if _status is True:
                num += 1
                subcat.subcategory_id = sub['cate_id']
                subcat.ordering = num
                subcat.save()
            print 'parent:', parent, 'subcat:', subcat, 'status:', _status
