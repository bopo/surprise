#  -*- coding: utf-8 -*-
from datetime import datetime

from django.core.paginator import Paginator

from restful.baichuan import FIELDS, get_detail
from restful.models.goods import Goods


def run():
    # 分页
    # collects = Collect.objects.filter(goods_ptr__item_img__isnull=True).order_by('id')
    # collects = Collect.objects.filter(goods_ptr__open_iid__isnull=True).order_by('id')
    collects = Goods.objects.filter(item_img__isnull=True)
    # collects = Collect.objects.all().order_by('id')
    paginator = Paginator(collects, 10)
    open_ids = []

    print paginator.count, paginator.num_pages, paginator.page_range

    if paginator.count == 0:
        print 'no found items.'
        return True

    for p in paginator.page_range:
        page = paginator.page(p)
        iids = []

        # 组合 num_iid
        for x in page.object_list:
            iids.append({'open_iid': str(x.open_iid), 'open_id': None})

        open_ids.append(iids)

    for k, open_id in enumerate(open_ids):
        if not open_id:
            continue

        item = get_detail(open_id)

        print k, item

        if item:
            print 'item loading...'
            for k, i in enumerate(item):

                if i.get('id'):
                    del i['id']

                if i is None:
                    continue

                objects = Goods.objects.filter(open_iid=i['open_iid']).get()

                for field in FIELDS:
                    if i.get(field) and field != 'id':
                        if field == 'delist_time':
                            i[field] = datetime.strptime(i[field], "%Y-%m-%d %H:%M:%S")

                        setattr(objects, field, i[field])

                objects.save()

                print k, 'objects.save()'
