'''
Created by auto_sdk on 2015.06.05
'''
from top.api.base import RestApi


class AtbItemsCouponGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.area = None
        self.cid = None
        self.coupon_type = None
        self.end_commission_num = None
        self.end_commission_rate = None
        self.end_commission_volume = None
        self.end_coupon_rate = None
        self.end_credit = None
        self.end_volume = None
        self.fields = None
        self.keyword = None
        self.page_no = None
        self.page_size = None
        self.shop_type = None
        self.sort = None
        self.start_commission_num = None
        self.start_commission_rate = None
        self.start_commission_volume = None
        self.start_coupon_rate = None
        self.start_credit = None
        self.start_volume = None

    def getapiname(self):
        return 'taobao.atb.items.coupon.get'
