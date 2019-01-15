# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from restful.helpers import send_verify_code
from .forms import SignupForm
from ..serializers import RegisterSerializer, VerifyMobileSerializer
from ..settings import TokenSerializer


class RegisterView(GenericAPIView):
    '''
    注意：

    手机注册前，先请求 `/auth/registration/verify_mobile/` 接口, 获取 verify code.

    请使用下面的正则表达式验证手机号码正确性，在提交服务器前客户端提交一次
    手机号码验证正则表达式：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
    '''
    token_model = Token
    form_class = SignupForm
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    response_serializer = TokenSerializer
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def form_valid(self, form):
        self.user = form.save(self.request)
        self.token, created = self.token_model.objects.get_or_create(user=self.user)
        return self.token

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.data)

        if self.form.is_valid():
            self.form_valid(self.form)
            return self.get_response()
        else:
            return self.get_response_with_errors()

    def get_response(self):
        serializer = self.response_serializer(instance=self.token)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_response_with_errors(self):
        return Response(self.form.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyMobileView(GenericAPIView):
    '''
    注意：

    请使用下面的正则表达式验证手机号码正确性，在提交服务器前客户端提交一次
    手机号码验证正则表达式：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
    '''
    response_serializer = TokenSerializer
    permission_classes = (AllowAny,)
    serializer_class = VerifyMobileSerializer
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def post(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')
        verify = send_verify_code(mobile)

        if not verify[0]:
            return Response({'errors': {'msgs': verify[1], 'code': 400}}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': u'验证码已经成功发送'}, status=status.HTTP_200_OK)
