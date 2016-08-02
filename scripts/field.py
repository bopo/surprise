# -*- coding: utf-8 -*-

import json
import os
import tempfile
from PIL import Image
import requests
from django.core.files import File

from restful.models.goods import GoodsCategory


def cover(url, crop=False):
    req = requests.get(url)
    tmp = tempfile.mktemp() + '.jpg'

    boxs = (22, 80, 162, 220)
    size = (142, 142)

    if req.status_code == 200:
        open(tmp, 'w').write(req.content)

        if crop:
            try:
                im = Image.open(tmp)
                region = im.crop(boxs)
                region.thumbnail(size)
                region.save(tmp, "JPEG")
            except IOError:
                print("cannot create thumbnail for", tmp)

        print tmp,
        print len(req.content)

        return File(open(tmp, 'rb'))
    else:
        return None


def run():
    for x in [90]:
        # 删除子分类
        for gc in GoodsCategory.objects.filter(parent_id=x).get_cached_trees():
            gc.delete()

        f = '%d.json' % x

        if not os.path.exists(f):
            continue

        t = open(f).read()
        t = json.loads(t)

        for i in t:
            print x, 'parent',
            cats = GoodsCategory()
            cats.cover = cover(i['parent'][1])
            cats.parent_id = x
            cats.name = i['parent'][0]
            print i['parent'][0], '-parent'

            if len(i['parent']) > 2:
                cats.keyword = i['parent'][2]

            cats.save()
            print cats.pk, cats.parent_id

            # 写入大图
            for s in i['items']:
                # 写入小图
                print x, 'items', s[1]
                item = GoodsCategory()
                item.cover = cover(s[1], True)
                item.parent_id = cats.pk
                item.name = s[0]
                print s[0], '-item'

                if len(s) > 2:
                    item.keyword = s[2]

                item.save()
                print item.pk, item.parent_id
