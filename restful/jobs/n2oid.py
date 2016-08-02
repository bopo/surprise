#  -*- coding: utf-8 -*-
from datetime import datetime

from django.core.paginator import Paginator
from django_extensions.management.jobs import BaseJob

from restful.baichuan import convert, FIELDS
from restful.models.goods import Collect


class Job(BaseJob):
    help = "Null open_iid items covert job."

    def execute(self):
        # 分页
        # collects = Collect.objects.filter(goods_ptr__item_img__isnull=True).order_by('id')
        # collects = Collect.objects.filter(goods_ptr__open_iid__isnull=True).order_by('id')
        collects = Collect.objects.filter(goods_ptr__item_img='[]')
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
                iids.append(str(x.num_iid))
                print x

            open_ids.append(iids)

        for k, open_id in enumerate(open_ids):
            if not open_id:
                continue

            item = convert(open_id, True)

            if not item:
                Collect.objects.filter(num_iid__in=open_id).delete()

            print k, item

            if item:
                print 'item loading...'
                for k, i in enumerate(item):

                    if i.get('id'):
                        del i['id']

                    if i is None:
                        continue

                    if i.get('bad'):
                        Collect.objects.filter(num_iid=i['open_id']).delete()
                        print 'bad items', i.get('title')
                        continue

                    objs = Collect.objects.filter(num_iid=i['open_id']).get()

                    if hasattr(objs, 'goods_ptr'):
                        for field in FIELDS:
                            if i.get(field) and field != 'id':
                                if field == 'delist_time':
                                    i[field] = datetime.strptime(i[field], "%Y-%m-%d %H:%M:%S")

                                setattr(objs.goods_ptr, field, i[field])

                        objs.goods_ptr.recommend = 1
                        objs.goods_ptr.save()
                        print 'objs.goods_ptr.save()'
