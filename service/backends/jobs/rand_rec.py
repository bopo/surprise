import random

from django_extensions.management.jobs import BaseJob

from restful.models.goods import Goods


class Job(BaseJob):
    help = "My sample job."

    def execute(self):

        for cid in (1, 2, 90):
            rs = Goods.objects.filter(category_recommend=cid).all()
            rt = range(rs.count())

            for x in rs:
                r = random.sample(rt, 1)[0]
                g, s = Goods.objects.get_or_create(pk=x.pk)
                g.ordering = r + 1
                g.save()
                rt.remove(r)
                print rt
