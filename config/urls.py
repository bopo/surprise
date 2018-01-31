# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.flatpages.views import flatpage

urlpatterns = (
    url(r'^share/extract/(?P<slug>.*)$', 'frontend.views.share_extract', name='share_extract'),
    url(r'^share/invite/(?P<slug>.*)$', 'frontend.views.share_invite', name='share_invite'),
    url(r'^share/qrcode/(?P<slug>.*)$', 'frontend.views.share_qrcode', name='share_qrcode'),
    url(r'^share/prize/(?P<slug>.*)$', 'frontend.views.share_prize', name='share_prize'),

    url(r'^r/(?P<mark>.*)$', 'frontend.views.r', name='r'),
    url(r'^q/(?P<uid>.*)$', 'frontend.views.q', name='q'),

    url(r'^$', 'frontend.views.home', name='home'),
    url(r'^help', 'frontend.views.help', name='help'),
    url(r'^packet$', 'frontend.views.packet', name='packet'),
    url(r'^packet/(?P<slug>.*)$', 'frontend.views.packet', name='packet'),
    url(r'^downloads/(?P<slug>.*)$', 'frontend.views.downloads', name='downloads'),
    url(r'^downapps$', 'frontend.views.downapps', name='downapps'),
    url(r'^oauth/wechat$', 'frontend.views.wechat'),

    url(r'^api/', include('restful.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    if ('debug_toolbar' in settings.INSTALLED_APPS):
        import debug_toolbar

        urlpatterns += (url(r'^__debug__/', include(debug_toolbar.urls)),)
# else:
#     urlpatterns += [
#         url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
#         url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permissin Denied")}),
#         url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
#         url(r'^500/$', default_views.server_error),
#     ]

urlpatterns += (
    # url(r'^(?P<url>.*/)$', flatpage),
)
