# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dynamic_scraper.spiders.django_checker import DjangoChecker

from restful.models.goods import GoodsItems


class GoodsChecker(DjangoChecker):
    name = 'goods_checker'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(GoodsItems, **kwargs)
        self.scraper = self.ref_object.collect_website.scraper
        # self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.checker_runtime
        super(GoodsChecker, self).__init__(self, *args, **kwargs)
