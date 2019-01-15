# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem

from .goods import GoodsCategory

BEST_RATE = settings.BEST_RATE


class CollectWebsite(models.Model):
    name = models.CharField(verbose_name=_(u'名称'), max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(GoodsCategory, blank=True, null=True)

    def __str__(self):
        return self.name

        # class Meta:
        #     verbose_name_plural = _(u'采集站点')
        #     verbose_name = _(u'采集站点')


class GoodsItems(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    pic_url = models.ImageField()
    auctionId = models.BigIntegerField(verbose_name=_(u'auctionId'), default=0)
    categoryId = models.BigIntegerField(verbose_name=_(u'categoryId'), default=0)
    detail_url = models.URLField(verbose_name=_('URL'))

    collect_website = models.ForeignKey(CollectWebsite, blank=True, null=True)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()


class GoodsItem(DjangoItem):
    django_model = GoodsItems

# @receiver(pre_delete)
# def pre_delete_handler(sender, instance, using, **kwargs):
#     if isinstance(instance, CollectWebsite):
#         if instance.scraper_runtime:
#             instance.scraper_runtime.delete()
#
#     if isinstance(instance, Goods):
#         if instance.checker_runtime:
#             instance.checker_runtime.delete()
#
#
# pre_delete.connect(pre_delete_handler)
