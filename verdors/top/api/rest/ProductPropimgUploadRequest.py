'''
Created by auto_sdk on 2012.10.15
'''
from top.api.base import RestApi


class ProductPropimgUploadRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.id = None
        self.image = None
        self.position = None
        self.product_id = None
        self.props = None

    def getapiname(self):
        return 'taobao.product.propimg.upload'

    def getMultipartParas(self):
        return ['image']
