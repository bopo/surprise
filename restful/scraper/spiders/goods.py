# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dynamic_scraper.spiders.django_spider import DjangoSpider

from restful.models.goods import CollectWebsite, GoodsItems, GoodsItem


class GoodsSpider(DjangoSpider):
    name = 'goods_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(CollectWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = GoodsItems
        self.scraped_obj_item_class = GoodsItem
        super(GoodsSpider, self).__init__(self, *args, **kwargs)
