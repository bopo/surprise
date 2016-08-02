'''
Created by auto_sdk on 2015.03.18
'''
from top.api.base import RestApi


class IselectItemsGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.page = None
        self.page_size = None
        self.tag_ids = None

    def getapiname(self):
        return 'taobao.iselect.items.get'
