# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import StatusModel
from model_utils.models import TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

BEST_RATE = settings.BEST_RATE


class TBKCategory(MPTTModel):
    '''
    name: "工作制服/校服",
    id: 50103026,
    type: "category",
    level: 1,
    count: "350",
    flag: "channel_fcat",
    subIds: null
    '''
    cid = models.BigIntegerField(_(u'ID'), blank=True, null=True)
    name = models.CharField(_(u'名称'), max_length=100, blank=False)
    type = models.CharField(_(u'类型'), max_length=100, blank=True, null=True)
    flag = models.CharField(_(u'标示'), max_length=100, blank=True, null=True)
    level = models.IntegerField(_(u'层级'), blank=True, null=True)
    count = models.IntegerField(_(u'count'), blank=True, null=True)
    subIds = models.IntegerField(_(u'子类'), blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    channel = models.CharField(_(u'频道'), max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class GoodsCategory(MPTTModel):
    name = models.CharField(verbose_name=_(u'分类名称'), max_length=64, null=False)
    slug = models.SlugField(verbose_name=_(u'Slug'), default='', blank=True, null=True)
    cover = models.ImageField(verbose_name=_(u'分类图片'), max_length=200, blank=True, upload_to='category')
    # cover = ProcessedImageField(verbose_name=_(u'分类图片'), upload_to='category', processors=[ResizeToFill(100, 100)],format='JPEG', null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    ordering = models.PositiveIntegerField(verbose_name=_(u'排序'), default=999, editable=False)
    is_active = models.BooleanField(verbose_name=_(u'激活'), default=False)
    keyword = models.CharField(verbose_name=_(u'分类关键字'), max_length=100, null=True, blank=True)
    channel = models.CharField(verbose_name=_(u'频道'), max_length=100, null=True, blank=True)
    catids = models.BigIntegerField(verbose_name=_(u'淘宝分类'), blank=True, null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'商品类别')
        verbose_name_plural = _(u'商品类别')

    class MPTTMeta:
        order_insertion_by = ['ordering']
        parent_attr = 'parent'

        # def save(self, *args, **kwargs):
        #     super(GoodsCategory, self).save(*args, **kwargs)
        #     GoodsCategory.objects.rebuild()


class Description(models.Model):
    open_iid = models.CharField(_(u'淘宝ID'), max_length=100, blank=True, null=True)
    content = models.TextField(_(u'描述信息'))


class Goods(StatusModel, TimeStampedModel):
    '''
        "open_iid":"abc",
        "seller_id":100,
        "nick":"jayzhou",
        "title":"1212",
        "price":"12.15",
        "item_location":"北京",
        "seller_credit_score":12,
        "pic_url":"http:\/\/img01.taobaocdn.com\/bao\/uploaded\/i1\/T1GM8KXkheXXXz9q_b_093149.jpg",

        "coupon_rate":"9500.00",
        "coupon_price":"25.50",
        "coupon_start_time":"2012-01-30 08:55:46",
        "coupon_end_time":"2013-08-31 08:56:01",

        "commission_rate":"500.00",
        "commission":"12.15",
        "commission_num":"123",
        "commission_volume":"12.15",
        "volume":100,
        "shop_type":"B",
        "promotion_price":"50.50"
    '''
    # open_iid,cid,title,desc,item_imgs,pic_url,promotion_price,price
    STATUS = Choices('draft', 'published')
    GENDER_CHOICES = (('male', '男'), ('female', '女'))
    CATEGORY_RECOMMEND = (('1', '男人'), ('2', '女人'), ('90', '潮童'))

    cid = models.IntegerField(verbose_name=_(u'淘宝分类ID'), blank=True, null=True)
    nick = models.CharField(verbose_name=_(u'卖家昵称'), max_length=100, blank=True, null=True)
    seller_id = models.IntegerField(verbose_name=_(u'卖家ID'), blank=True, null=True)
    item_location = models.CharField(verbose_name=_(u'商品所在地'), max_length=100, blank=True, null=True)
    seller_credit_score = models.IntegerField(verbose_name=_(u'卖家信用等级'), blank=True, null=True)

    commission = models.CharField(verbose_name=_(u'淘宝客佣金'), max_length=255, blank=True, null=True)
    commission_num = models.CharField(verbose_name=_(u'累计成交量'), max_length=255, blank=True, null=True)
    commission_rate = models.CharField(verbose_name=_(u'淘宝客佣金比率'), max_length=255, blank=True, null=True)
    commission_volume = models.CharField(verbose_name=_(u'累计总支出佣金量'), max_length=255, blank=True, null=True)

    coupon_rate = models.DecimalField(verbose_name=_(u'折扣比率'), decimal_places=2, max_digits=10, blank=True, null=True)
    coupon_price = models.DecimalField(verbose_name=_(u'折扣价格'), decimal_places=2, max_digits=10, blank=True, null=True)
    coupon_start_time = models.DateTimeField(verbose_name=_(u'折扣活动开始时间'), blank=True, null=True)
    coupon_end_time = models.DateTimeField(verbose_name=_(u'折扣活动结束时间'), blank=True, null=True)

    promotion_price = models.CharField(verbose_name=_(u'促销价'), max_length=255, blank=True, null=True)
    volume = models.CharField(verbose_name=_(u'30天内交易量'), max_length=255, blank=True, null=True)
    pic_url = models.URLField(verbose_name=_(u'图片url'), max_length=255, blank=True, null=True)
    item_img = models.TextField(verbose_name=_(u'多张图片'), max_length=255, blank=True, null=True)
    shop_type = models.CharField(verbose_name=_(u'店铺类型:B(商城),C(集市)'), max_length=2, blank=True, null=True, default='C')

    open_iid = models.CharField(verbose_name=_(u'商品ID'), max_length=255, blank=True, null=True)
    title = models.CharField(verbose_name=_(u'标题'), max_length=255, blank=True, null=True)
    price = models.DecimalField(verbose_name=_(u'原价格'), max_digits=10, decimal_places=2, blank=True, null=True)
    # saved = models.DecimalField(verbose_name=_(u'节省价格'), max_digits=10, decimal_places=2, blank=True, null=True,
    #     default='0.00')

    category = models.ForeignKey(GoodsCategory, verbose_name=_(u'商品分类'), null=True)
    recommend = models.BooleanField(verbose_name=_(u'是否推荐'), default=False)
    besting = models.BooleanField(verbose_name=_(u'是否"惊"推荐'), default=False)

    gender = models.CharField(verbose_name=_(u'性别'), max_length=20, choices=GENDER_CHOICES, default='female')
    delist_time = models.DateTimeField(verbose_name=_(u'下架时间'), blank=True, null=True)
    # description = models.OneToOneField(Description, blank=True, null=True, verbose_name=_(u'详细信息'))
    category_recommend = models.CharField(_('分类推荐'), max_length=10, blank=True, null=True, choices=CATEGORY_RECOMMEND)
    ordering = models.IntegerField(_('排序'), default=99999)

    @property
    def location(self):
        return self.item_location

    # 折扣节省
    @property
    def saved(self):
        self.promotion_price = self.price
        if self.commission_rate is None:
            self.commission_rate = 300
        return round(float(self.promotion_price) * float(float(self.commission_rate) / 10000.00 * BEST_RATE), 2)

    # 折扣比例 数字型
    @property
    def rated(self):
        if self.commission_rate is None:
            self.commission_rate = 300
        return float(float(self.commission_rate) / 10000.00 * BEST_RATE)

    # 折扣比例 字符串
    @property
    def rate(self):
        if self.commission_rate is None:
            self.commission_rate = 300
        return str(float(float(self.commission_rate) / 10000.00 * BEST_RATE) * 100) + '%'

    # 折扣价格
    @property
    def best(self):
        # @todo 临时
        self.promotion_price = self.price
        return round(float(self.promotion_price) - self.saved, 2)

    @property
    def thumb(self):
        if self.pic_url:
            return self.pic_url + "_" + settings.THUMB_LIST + ".jpg"

    @property
    def item_imgs(self):
        try:
            imgs = json.loads(self.item_img)
            for k, v in enumerate(imgs):
                imgs[k]['url'] = v['url'] + "_" + settings.THUMB_LIST + ".jpg"
            return imgs
        except Exception, e:
            return None

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name_plural = _(u'商品列表')
        verbose_name = _(u'商品列表')


class QueryHistory(Goods):
    class Meta:
        verbose_name_plural = _(u'搜索历史')
        verbose_name = _(u'搜索历史')


class QueryRule(models.Model):
    '''
    area	String	可选	杭州		商品所在地
    auto_send	String	可选	true		是否自动发货
    cid	Number	特殊可选	123		标准商品后台类目id。该ID可以通过taobao.itemcats.get接口获取到。
    end_commission_num	String	可选	10000		30天累计推广量（与返回数据中的commission_num字段对应）上限.
    end_commission_rate	String	可选	2345		佣金比率上限，如：2345表示23.45%。注：start_commissionRate和end_commissionRate一起设置才有效。
    end_credit	String	可选	1heart		可选值和start_credit一样.start_credit的值一定要小于或等于end_credit的值。注：end_credit与start_credit一起使用才生效
    end_price	String	可选	999		最高价格
    end_totalnum	String	可选	10		商品总成交量（与返回字段volume对应）上限。
    fields	String []	必须	open_iid 最大列表长度：20 需返回的字段列表.可选值:open_iid,title,nick,pic_url,price,commission,commission_rate,commission_num,commission_volume,seller_credit_score,item_location,volume ;字段之间用","分隔
    guarantee	String	可选	true		是否查询消保卖家
    real_describe	String	可选	true		是否如实描述(即:先行赔付)商品，设置为true表示该商品是如实描述的商品，设置为false或不设置表示不判断这个属性
    keyword	String	特殊可选	abc		商品标题中包含的关键字. 注意:查询时keyword,cid至少选择其中一个参数
    cash_coupon	String	可选	true		是否支持抵价券，设置为true表示该商品支持抵价券，设置为false或不设置表示不判断这个属性
    vip_card	String	可选	true		是否支持VIP卡，设置为true表示该商品支持VIP卡，设置为false或不设置表示不判断这个属性
    page_no	Number	可选	1 默认值：1 结果页数.1~10 支持最大值为：10
    page_size	Number	可选	40 默认值：40 每页返回结果数.最大每页40 支持最大值为：400
    overseas_item	String	可选	true 默认值：false 是否海外商品，设置为true表示该商品是属于海外商品，默认为false
    onemonth_repair	String	可选	true		是否30天维修，设置为true表示该商品是支持30天维修，设置为false或不设置表示不判断这个属性
    sevendays_return 	String	可选	true		是否支持7天退换，设置为true表示该商品支持7天退换，设置为false或不设置表示不判断这个属性
    sort	String	可选	price_desc		默认排序:default price_desc(价格从高到低) price_asc(价格从低到高) credit_desc(信用等级从高到低) commissionRate_desc(佣金比率从高到低) commissionRate_asc(佣金比率从低到高) commissionNum_desc(成交量成高到低) commissionNum_asc(成交量从低到高) commissionVolume_desc(总支出佣金从高到低) commissionVolume_asc(总支出佣金从低到高) delistTime_desc(商品下架时间从高到低) delistTime_asc(商品下架时间从低到高)
    start_commission_num	String	可选	1000		30天累计推广量（与返回数据中的commission_num字段对应）下限.注：该字段要与end_commissionNum一起使用才生效
    start_commission_rate	String	可选	1234		佣金比率下限，如：1234表示12.34%
    start_credit	String	可选	1heart		卖家信用: 1heart(一心) 2heart (两心) 3heart(三心) 4heart(四心) 5heart(五心) 1diamond(一钻) 2diamond(两钻 3diamond(三钻) 4diamond(四钻) 5diamond(五钻) 1crown(一冠) 2crown(两冠) 3crown(三冠) 4crown(四冠) 5crown(五冠) 1goldencrown(一黄冠) 2goldencrown(二黄冠) 3goldencrown(三黄冠) 4goldencrown(四黄冠) 5goldencrown(五黄冠)
    start_price	String	可选	1		起始价格.传入价格参数时,需注意起始价格和最高价格必须一起传入,并且 start_price <= end_price
    start_totalnum	String	可选	1		商品总成交量（与返回字段volume对应）下限。
    support_cod	String	可选	true		是否支持货到付款，设置为true表示该商品是支持货到付款，设置为false或不设置表示不判断这个属性
    mall_item	String	可选	true		是否商城的商品，设置为true表示该商品是属于淘宝商城的商品，设置为false或不设置表示不判断这个属性
    '''
    STATUS = Choices('draft', 'published')
    CREDIT_CHOICES = (
        ('1heart', u'一心'),
        ('2heart', u'两心'),
        ('3heart', u'三心'),
        ('4heart', u'四心'),
        ('5heart', u'五心'),
        ('1diamond', u'一钻'),
        ('2diamond', u'两钻'),
        ('3diamond', u'三钻'),
        ('4diamond', u'四钻'),
        ('5diamond', u'五钻'),
        ('1crown', u'一冠'),
        ('2crown', u'两冠'),
        ('3crown', u'三冠'),
        ('4crown', u'四冠'),
        ('5crown', u'五冠'),
        ('1goldencrown', u'一黄冠'),
        ('2goldencrown', u'二黄冠'),
        ('3goldencrown', u'三黄冠'),
        ('4goldencrown', u'四黄冠'),
        ('5goldencrown', u'五黄冠'),
    )
    SORT_CHOICES = (
        ('price_desc', u'价格从高到低'),
        ('price_asc', u'价格从低到高'),
        ('credit_desc', u'信用等级从高到低'),
        ('commissionRate_desc', u'佣金比率从高到低'),
        ('commissionRate_asc', u'佣金比率从低到高'),
        ('commissionNum_desc', u'成交量成高到低'),
        ('commissionNum_asc', u'成交量从低到高'),
        ('commissionVolume_desc', u'总支出佣金从高到低'),
        ('commissionVolume_asc', u'总支出佣金从低到高'),
        ('delistTime_desc', u'商品下架时间从高到低'),
        ('delistTime_asc', u'商品下架时间从低到高'),
    )
    # area = models.CharField(verbose_name=_(u'商品所在地'), null=True, blank=True, max_length=100)
    # auto_send = models.BooleanField(verbose_name=_(u'是否自动发货'), default=0)
    # cid = models.IntegerField(
    #     verbose_name=_(u'标准商品后台类目id'),
    #     help_text=_(u'该ID可以通过taobao.itemcats.get接口获取到。'),
    #     blank=True,
    #     null=True
    # )
    sort = models.CharField(
        verbose_name=_(u'默认排序'),
        null=True, max_length=100, choices=SORT_CHOICES)

    start_commission_num = models.CharField(
        verbose_name=_(u'最低30天累计推广量'), help_text=_(u'（与返回数据中的commission_num字段对应）下限.注：该字段要与end_commissionNum一起使用才生效'),
        null=True, max_length=100)

    end_commission_num = models.CharField(
        verbose_name=_(u'最高30天累计推广量'),
        help_text=_(u'（与返回数据中的commission_num字段对应）上限.'),
        null=True,
        blank=True,
        max_length=100)

    start_commission_rate = models.CharField(verbose_name=_(u'最低佣金比率'), help_text=_(u'如：1234表示12.34%'), blank=True,
        null=True,
        max_length=100)

    end_commission_rate = models.CharField(
        verbose_name=_(u'最高佣金比率'),
        help_text=_(u'如：2345表示23.45%。注：start_commissionRate和end_commissionRate一起设置才有效。'),
        null=True,
        blank=True,
        max_length=100)

    start_credit = models.CharField(verbose_name=_(
        u'最低卖家信用'), blank=True,
        null=True, max_length=100, choices=CREDIT_CHOICES)

    end_credit = models.CharField(verbose_name=_(u'最高卖家信用'),
        help_text=_(u'可选值和start_credit一样.start_credit的值一定要小于或等于end_credit的值。注：end_credit与start_credit一起使用才生效'),
        null=True,
        blank=True,
        max_length=100,
        choices=CREDIT_CHOICES)

    start_price = models.CharField(
        verbose_name=_(u'起始价格'),
        help_text=_(u'传入价格参数时,需注意起始价格和最高价格必须一起传入,并且 start_price <= end_price'),
        blank=True,
        null=True,
        max_length=100)

    end_price = models.CharField(
        verbose_name=_(u'最高价格'),
        null=True,
        blank=True,
        max_length=100)

    start_totalnum = models.CharField(
        verbose_name=_(u'商品总成交量'),
        help_text=_(u'（与返回字段volume对应）下限。'), null=True, blank=True,
        max_length=100)

    end_totalnum = models.CharField(
        verbose_name=_(u'商品总成交量'),
        help_text=_(u'（与返回字段volume对应）上限。'),
        null=True,
        blank=True,
        max_length=100)

    guarantee = models.BooleanField(
        verbose_name=_(u'是否查询消保卖家'),
        help_text=_(u'可选参数, 默认true'),
        default=0)

    # real_describe = models.BooleanField(
    #     verbose_name=_(u'是否如实描述'),
    #     help_text=_(u'（与返回字段volume对应）上限。'),
    #     default=0)
    # keyword = models.CharField(
    #     verbose_name=_(u'商品标题中包含的关键字'),
    #     help_text=_(u' 注意:查询时keyword,cid至少选择其中一个参数'), null=True,
    #     max_length=100)
    # cash_coupon = models.BooleanField(
    #     verbose_name=_(u'是否支持抵价券'),
    #     help_text=_(u'设置为true表示该商品支持抵价券，设置为false或不设置表示不判断这个属性'),
    #     default=0)
    # vip_card = models.BooleanField(
    #     verbose_name=_(u'是否支持VIP卡'),
    #     help_text=_(u'设置为true表示该商品支持VIP卡，设置为false或不设置表示不判断这个属性'),
    #     default=0)
    # page_no = models.IntegerField(verbose_name=_(u'分页页码'), blank=True, null=True)
    # page_size = models.IntegerField(verbose_name=_(u'分页大小'), blank=True, null=True)
    # overseas_item = models.BooleanField(verbose_name=_(u'是否海外商品'),
    #     help_text=_(u'设置为true表示该商品是属于海外商品，默认为false'))

    # onemonth_repair = models.BooleanField(
    #     verbose_name=_(u'是否30天维修'),
    #     help_text=_(u'设置为true表示该商品是支持30天维修，设置为false或不设置表示不判断这个属性'),
    #     default=0)

    # sevendays_return = models.BooleanField(
    #     verbose_name=_(u'是否支持7天退换'),
    #     help_text=_(u'设置为true表示该商品支持7天退换，设置为false或不设置表示不判断这个属性'),
    #     default=0)

    mall_item = models.BooleanField(
        verbose_name=_(u'是否商城的商品'),
        help_text=_(u'设置为true表示该商品是属于淘宝商城的商品，设置为false或不设置表示不判断这个属性'),
        default=0)

    def __unicode__(self):
        return '搜索规则设置'

    class Meta:
        verbose_name_plural = _(u'搜索规则')
        verbose_name = _(u'搜索规则')


class PreselectionCategory(MPTTModel):
    PRESELECTION_CHOICES = (
        ('nanyibang', u'男衣邦'),
        ('liwushuo', u'礼物说'),
    )
    name = models.CharField(verbose_name=_(u'分类名称'), max_length=64, null=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    source = models.CharField(_(u'采集点'), max_length=100, default=None, blank=True, choices=PRESELECTION_CHOICES)
    category = models.ForeignKey(GoodsCategory, verbose_name=_(u'商品分类'), null=True)
    ordering = models.IntegerField(verbose_name=_(u'排序'), default=999)
    subcategory_id = models.IntegerField(verbose_name=_(u'采集分类'), default=0)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'采集类别关联')
        verbose_name_plural = _(u'采集类别关联')

    class MPTTMeta:
        order_insertion_by = ['ordering']

    def save(self, *args, **kwargs):
        super(PreselectionCategory, self).save(*args, **kwargs)
        PreselectionCategory.objects.rebuild()


class Preselection(StatusModel, TimeStampedModel):
    STATUS = Choices('draft', 'published')
    source = models.CharField(_(u'采集点'), max_length=100, default=None, blank=True, null=True)
    num_iid = models.BigIntegerField(verbose_name=_(u'淘宝真实ID'), blank=True, null=True)
    nick = models.CharField(verbose_name=_(u'卖家昵称'), max_length=100, blank=True, null=True)

    commission = models.CharField(verbose_name=_(u'淘宝客佣金'), max_length=255, blank=True, null=True)
    commission_num = models.CharField(verbose_name=_(u'累计成交量'), max_length=255, blank=True, null=True)
    commission_rate = models.CharField(verbose_name=_(u'淘宝客佣金比率'), max_length=255, blank=True, null=True)
    commission_volume = models.CharField(verbose_name=_(u'累计总支出佣金量'), max_length=255, blank=True, null=True)

    promotion_price = models.CharField(verbose_name=_(u'促销价格'), max_length=255, blank=True, null=True)
    volume = models.CharField(verbose_name=_(u'30天内交易量'), max_length=255, blank=True, null=True)
    pic_url = models.URLField(verbose_name=_(u'图片url'), max_length=255, blank=True, null=True)
    shop_type = models.CharField(verbose_name=_(u'店铺类型:B(商城),C(集市)'), max_length=2, blank=True, null=True, default='C')

    title = models.CharField(verbose_name=_(u'标题'), max_length=255, blank=True, null=True)
    price = models.DecimalField(verbose_name=_(u'价格'), max_digits=10, decimal_places=2, blank=True, null=True)
    delist_time = models.DateTimeField(verbose_name=_(u'下架时间'), blank=True, null=True)

    category = models.CharField(verbose_name=_(u'采集父分类'), max_length=255, blank=True, null=True)
    category_id = models.IntegerField(verbose_name=_(u'采集父分类ID'), blank=True, null=True)

    subcategory = models.CharField(verbose_name=_(u'采集子分类'), max_length=255, blank=True, null=True)
    subcategory_id = models.IntegerField(verbose_name=_(u'采集子分类ID'), blank=True, null=True)


class Collect(Goods):
    '''
       "530835666525" : {
      "from_name" : "阿里妈妈",

      "zk" : "3.5",
      "check" : 1,
      "picurl2" : "http://img.alicdn.com/imgextra/i2/TB1bMA8JpXXXXXTXXXXXXXXXXXX_!!0-item_pic.jpg",
      "ly" : "啊打发打发",
      "yh_price" : "58.0",
      "bili" : "",
      "from_host" : "",
      "sid" : "69676416",
      "start_time" : "",
      "picurl" : "http://img.alicdn.com/imgextra/i2/TB1bMA8JpXXXXXTXXXXXXXXXXXX_!!0-item_pic.jpg",
      "nick" : "墨锦服饰旗舰店",
      "baoyou" : 1,
      "price" : "58.0010.50%￥6.09",
      "title" : "墨锦2016夏季新款五分袖原宿风大V领条纹衬衫女装宽松小清新上衣",
      "title2" : "墨锦2016夏季新款五分袖原宿风大V领条纹衬衫女装宽松小清新上衣",
      "end_time" : "",
      "shop_type" : 1,
      "url" : "http://item.taobao.com/item.htm?id=530835666525",
      "cate" : "0",
      "images" : [
         "http://img.alicdn.com/imgextra/i2/TB1bMA8JpXXXXXTXXXXXXXXXXXX_!!0-item_pic.jpg",
         "http://img.alicdn.com/imgextra/i2/792536009/TB2cxPjnVXXXXahXpXXXXXXXXXX_!!792536009.jpg",
         "http://img.alicdn.com/imgextra/i1/792536009/TB2aUDvnVXXXXb6XXXXXXXXXXXX_!!792536009.jpg",
         "http://img.alicdn.com/imgextra/i2/792536009/TB2nky_nVXXXXcgXpXXXXXXXXXX_!!792536009.jpg",
         "http://img.alicdn.com/imgextra/i3/792536009/TB206W3nVXXXXcDXpXXXXXXXXXX_!!792536009.jpg"
      ],
      "fid" : "0",
      "shop_url" : "http://store.taobao.com/shop/view_shop.htm?user_number_id=792536009",
      "num" : "958",
      "from_url" : "",
      "cid" : "162104",
      "zkType" : "手机折扣",
      "sum" : "2632",
      "num_iid" : "530835666525",
      "commission" : ""
   }'''
    STATUS = Choices('ready', 'error', 'done')
    # category = models.ForeignKey(GoodsCategory, verbose_name=_(u'商品分类'), null=True)

    from_name = models.CharField(verbose_name=_(u'标题'), max_length=255, blank=True, null=True)
    # title = models.CharField(verbose_name=_(u'标题'), max_length=255, blank=True, null=True)
    # price = models.DecimalField(verbose_name=_(u'价格'), max_digits=10, decimal_places=2, blank=True, null=True)

    # pic_url = models.URLField(verbose_name=_(u'图片url'), max_length=255, blank=True, null=True)
    num_iid = models.BigIntegerField(verbose_name=_(u'商品真id'), blank=True, null=True)
    coverted = models.BooleanField(verbose_name=_(u'转换'), default=0)

    # images = models.TextField()

    class Meta:
        ordering = ('-created',)
        verbose_name = _(u'采集临时库')
        verbose_name_plural = _(u'采集临时库')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()
