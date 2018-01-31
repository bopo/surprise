# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from restful.models.goods import GoodsCategory, Goods


def get_children(obj):
    sub = obj.get_children()
    cid = [obj.id]
    cid.extend([x.id for x in sub])

    for x in sub:
        cid.extend(get_children(x))

    print obj.get_level(), cid

    total = Goods.objects.filter(category__in=cid).count()
    obj.total = total
    obj.save()

    return cid


def run():
    cats = GoodsCategory.objects.filter(level=0)

    for cat in cats:
        get_children(cat)
