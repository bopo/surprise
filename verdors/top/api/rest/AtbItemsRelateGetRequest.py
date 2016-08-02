'''
Created by auto_sdk on 2014.10.11
'''
from top.api.base import RestApi


class AtbItemsRelateGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.cid = None
        self.fields = None
        self.max_count = None
        self.open_iid = None
        self.relate_type = None
        self.seller_id = None
        self.shop_type = None
        self.sort = None

    def getapiname(self):
        return 'taobao.atb.items.relate.get'
