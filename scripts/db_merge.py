# -*- coding: utf-8 -*-
import requests, json
from restful.models.goods import Collect,Goods


def run():
    dbs = 'database/backups/2016080811/004_restful.goods.json'
    dbs = open(dbs).read()
    dbs = json.loads(dbs)
    res = []

    for x in dbs:
        obj, s = Goods.objects.get_or_create(pk=x.get('pk'))

        if s:
            # 写入数据库
            res.append(x)
            print x.get('field').get('title')

            # for field, value in x.get('field').items():
            #     setattr(obj, field, value)

            # obj.save()

    res = json.dumps(res)    
    fle = open('db_merge.json', 'w')

    fle.write(res)
    fle.close()
