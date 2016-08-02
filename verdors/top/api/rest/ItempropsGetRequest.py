'''
Created by auto_sdk on 2016.03.30
'''
from top.api.base import RestApi


class ItempropsGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.attr_keys = None
        self.child_path = None
        self.cid = None
        self.datetime = None
        self.fields = None
        self.is_color_prop = None
        self.is_enum_prop = None
        self.is_input_prop = None
        self.is_item_prop = None
        self.is_key_prop = None
        self.is_sale_prop = None
        self.parent_pid = None
        self.pid = None
        self.type = None

    def getapiname(self):
        return 'taobao.itemprops.get'
