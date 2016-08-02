#  -*- coding: utf-8 -*-
from datetime import datetime

from django.core.paginator import Paginator

from restful.baichuan import convert, FIELDS
from restful.models.goods import Collect


def run():
    collects = Collect.objects.filter(goods_ptr__open_iid__isnull=True)
    paginator = Paginator(collects, 10)
    print paginator.count, paginator.num_pages, paginator.page_range

    for p in paginator.page_range:
        page = paginator.page(p)
        iids = []

        print p, 'page..', page.object_list

        for x in page.object_list:
            iids.append(str(x.num_iid))
            print x.num_iid

        if iids:
            item = convert(iids, True)
            print iids

            if item:
                for k, i in enumerate(item):

                    if i is None:
                        continue

                    print p, paginator.num_pages, i.get('open_id')
                    objs = Collect.objects.filter(num_iid=i['open_id']).get()

                    if hasattr(objs, 'good_ptr'):
                        for field in FIELDS:
                            if i.get(field):
                                if field == 'delist_time':
                                    i[field] = datetime.strptime(i[field], "%Y-%m-%d %H:%M:%S")

                                setattr(objs.goods_ptr, field, i[field])

                        objs.goods_ptr.save()
                        print p, objs
                    else:
                        objs.delete()
