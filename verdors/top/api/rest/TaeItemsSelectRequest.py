'''
Created by auto_sdk on 2016.01.11
'''
from top.api.base import RestApi


class TaeItemsSelectRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.cid = None
        self.end_price = None
        self.fields = None
        self.modified_time = None
        self.page_no = None
        self.page_size = None
        self.seller_cids = None
        self.seller_nick = None
        self.start_price = None

    def getapiname(self):
        return 'taobao.tae.items.select'
