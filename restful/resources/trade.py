# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from import_export import resources

from restful.models.trade import Trade


class TradeResource(resources.ModelResource):
    class Meta:
        model = Trade
