# -*- coding: utf-8 -*-
import json
import time
from datetime import datetime
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.core.paginator import Paginator
from django.utils.timezone import now

from restful.models.goods import Goods, Description, GoodsCategory
from restful.utils import top_items, top_detail


class Command(BaseCommand):
    help = 'Collect goods api.'

    option_list = BaseCommand.option_list + (
        make_option('--expire', action='store_true', dest='expire', default=False),
        make_option('--sleep', action='store', dest='sleep', default=0.7),
        make_option('--sync', action='store_true', dest='sync', default=False),
        make_option('--desc', action='store_true', dest='desc', default=False),
    )

    # def add_arguments(self, parser):
    #     parser.add_argument('args', metavar='app_label', nargs='*')
    #     parser.add_argument(
    #         '--tag', '-t', action='append', dest='tags',
    #         help='Run only checks labeled with given tag.',
    #     )
    #     parser.add_argument(
    #         '--list-tags', action='store_true', dest='list_tags',
    #         help='List available tags.',
    #     )
    #     parser.add_argument(
    #         '--deploy', action='store_true', dest='deploy',
    #         help='Check deployment settings.',
    #     )
    #     parser.add_argument(
    #         '--fail-level',
    #         default='ERROR',
    #         choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'],
    #         dest='fail_level',
    #         help=(
    #             'Message level that will cause the command to exit with a '
    #             'non-zero status. Default is ERROR.'
    #         ),
    #     )

    def handle(self, *args, **options):
        '''
        Args:
            *args:
            **options:

        Returns:

        '''

        GOODS_COLUMN = [field.column for field in Goods._meta.fields]

        open_iids = []

        expire = float(options['expire']) if options['expire'] else False
        sleep = float(options['sleep']) if options['sleep'] else 0.3

        sync = float(options['sync']) if options['sync'] else False
        desc = float(options['desc']) if options['desc'] else False

        if expire:
            # 删除过期数据
            print '  >> delete goods for expired...',
            # Goods.objects.all().delete()
            Goods.objects.filter(delist_time__lte=now()).delete()
            print 'done!'

        if sync:
            for gc in GoodsCategory.objects.filter(parent_id__gt=0):
                keyword = gc.keyword.encode('utf-8')
                items = top_items(keyword, sleep=sleep)

                if items is not None:

                    for key, item in items.items():
                        instance, status = Goods.objects.get_or_create(open_iid=item.get('open_iid'))
                        instance.category_id = gc.pk

                        for field in GOODS_COLUMN:
                            if item.get(field):
                                setattr(instance, field, item[field])

                        instance.save()
                        print instance.title, instance.price

                        open_iids.append(instance.open_iid)

        if desc:
            # 采集没有详细信息的产品
            print ' >> 采集没有详细信息的产品'
            goods = Goods.objects.filter(description=None)
            items = Paginator(goods, 10)

            if not items.num_pages:
                return None

            for page in items.page_range:
                time.sleep(sleep)

                item = items.page(page)
                iids = [x.open_iid for x in item.object_list]
                data = top_detail(iids)

                if data is None:
                    CommandError('not found item detail.')
                    continue

                for item in data:
                    instance, status = Goods.objects.get_or_create(open_iid=item.get('open_iid'))

                    for field in GOODS_COLUMN:
                        if item.get(field):
                            if field == 'delist_time':
                                item[field] = datetime.strptime(item[field], "%Y-%m-%d %H:%M:%S")

                            if field == 'item_imgs':
                                item[field] = json.dumps(item[field])
                                print item[field]

                            setattr(instance, field, item[field])

                    description, status = Description.objects.get_or_create(open_iid=item.get('open_iid'))
                    description.content = item.get('desc')
                    description.save()

                    instance.description = description
                    instance.save()

                    print '[%d/%d] %s' % (page, items.num_pages, instance.title)
