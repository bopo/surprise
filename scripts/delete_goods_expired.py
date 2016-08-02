from django.utils.timezone import now

from restful.models.goods import Goods


def run():
    Goods.objects.filter(delist_time__lte=now()).delete()
    # GoodsCategory.objects.filter(catids__in=['19254', '19246', '19253', '19257', '19260']).delete()
