# -*- coding: utf-8 -*-
import json

import short_url
from PIL import Image
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework.reverse import reverse
from wechatpy import WeChatOAuth

from config.settings.setup import MEDIA_ROOT
from restful.models.goods import Goods, GoodsCategory
from restful.utils import createQRCode, text2img, watermark

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


@cache_page(60 * 15)
def home(request):
    recommend = Goods.objects.order_by('-id').filter(recommend=1).all()[:10]
    category = GoodsCategory.objects.all()

    return render(request, 'index.html', locals())


# @cache_page(60 * 15)
def help(request):
    return render(request, 'help.html', locals())


@cache_page(60 * 15)
def detail(request, id):
    return render(request, 'detail.html', locals())


@cache_page(60 * 15)
def brand(request):
    return render(request, 'brand.html', locals())


@cache_page(60 * 15)
def sales(request):
    return render(request, 'sales.html', locals())


@cache_page(60 * 15)
def offer(request):
    return render(request, 'offer.html', locals())


@cache_page(60 * 15)
def apps(request):
    return render(request, 'apps.html', locals())


def packet(request):
    from restful.tasks import _do_kground_work
    _do_kground_work.delay('GreenPine')
    return render(request, 'packet.html', locals())


def share_extract(request, slug=None):
    return render(request, 'share/invite.html', locals())


def share_invite(request, slug=None):
    return render(request, 'share/invite.html', locals())


def share_qrcode(request, slug=None):
    url = reverse(viewname='downloads', request=request, args=[slug])
    buf = StringIO()

    text = u'我是你的朋友, 我邀请你加入够惊喜'
    image = Image.open(MEDIA_ROOT + '/thumb_IMG_0215_1024.jpg')
    image = watermark(image, createQRCode(url), ('center', 527))
    image = watermark(image, text2img(text=text), ('center', 427))

    if image:
        image.save(buf, 'png')
        value = buf.getvalue()
        return HttpResponse(value, content_type="image/jpeg")
    else:
        print "Sorry, Failed."


def share_prize(request, slug=None):
    return render(request, 'share/invite.html', locals())


def downloads(request, slug=None):
    android_url = settings.DOWNLOAD_ANDROID
    ios_url = settings.DOWNLOAD_IOS
    return render(request, 'downloads.html', locals())
    # itunes = 'https://itunes.apple.com/us/app/gou-jing-xi/id1089420214?l=zh&ls=1&mt=8'
    # return HttpResponseRedirect(redirect_to=itunes)


def downapps(request):
    android_url = settings.DOWNLOAD_ANDROID
    ios = settings.DOWNLOAD_IOS

    # return render(request, 'downloads.html', locals())


def r(request, mark):
    print mark
    return HttpResponse(mark)


def q(request, uid):
    uid = short_url.decode_url(uid)
    url = 'http://' + request.get_host() + '/r/%s' % uid
    img = createQRCode(url)
    buf = StringIO()
    img.save(buf)

    stream = buf.getvalue()
    return HttpResponse(stream, content_type="image/jpeg")


def wechat(request):
    redirect_uri = 'http://oauth.gjingxi.com/oauth/wechat/'

    codes = request.GET.get('code', None)
    oauth = WeChatOAuth(settings.WECHAT_APPKEY.strip(), settings.WECHAT_SECRET, redirect_uri=redirect_uri,
        scope='snsapi_userinfo')

    if codes is None:
        return HttpResponseRedirect(oauth.authorize_url)
    try:
        access = oauth.fetch_access_token(codes)
        oauth.refresh_access_token(access.get('refresh_token'))
        user = oauth.get_user_info()

        return HttpResponse(json.dumps(user))
    except Exception as e:
        print e
        return HttpResponse(e.message)
