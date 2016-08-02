'''
Created by auto_sdk on 2014.10.11
'''
from top.api.base import RestApi


class AtbItemsGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.area = None
        self.auto_send = None
        self.cash_coupon = None
        self.cid = None
        self.end_commission_num = None
        self.end_commission_rate = None
        self.end_credit = None
        self.end_price = None
        self.end_totalnum = None
        self.fields = None
        self.guarantee = None
        self.keyword = None
        self.mall_item = None
        self.onemonth_repair = None
        self.overseas_item = None
        self.page_no = None
        self.page_size = None
        self.real_describe = None
        self.sevendays_return = None
        self.sort = None
        self.start_commission_num = None
        self.start_commission_rate = None
        self.start_credit = None
        self.start_price = None
        self.start_totalnum = None
        self.support_cod = None
        self.vip_card = None

    def getapiname(self):
        return 'taobao.atb.items.get'
