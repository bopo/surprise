# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from restful.helpers import send_verify_code
from .settings import (
    LoginSerializer, PasswordChangeSerializer, PasswordResetConfirmSerializer,
    PasswordResetSerializer, TokenSerializer, UserDetailsSerializer
)


class SocialView(GenericAPIView):
    '''
    如果用户登陆状态则为绑定
    如果用户为登陆状态则为登陆
    如果用户之前没有注册，则为注册并绑定
    用户名则为随机生成
    用户以手机号为主要登陆方式
    '''
    token_model = Token
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    response_serializer = TokenSerializer
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_response(self):
        return Response(self.response_serializer(self.token).data, status=status.HTTP_200_OK)

    def get_error_response(self):
        return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=self.request.data)

        if not self.serializer.is_valid():
            return self.get_error_response()

        self.login()
        return self.get_response()


class LoginView(GenericAPIView):
    """
    POST 提交参数: mobile, password,
    返回的 key 是 toke n的值.

    请使用下面的正则表达式验证手机号码正确性，在提交服务器前客户端提交一次
    手机号码验证正则表达式：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
    """
    token_model = Token
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    response_serializer = TokenSerializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.token, created = self.token_model.objects.get_or_create(user=self.user)

        if self.serializer.validated_data.get('jpush_registration_id'):
            self.user.jpush_registration_id = self.serializer.validated_data.get('jpush_registration_id')
            self.user.save()

        # print self.serializer.validated_data

        if getattr(settings, 'REST_SESSION_LOGIN', True):
            login(self.request, self.user)

    def get_response(self):
        return Response(self.response_serializer(self.token).data, status=status.HTTP_200_OK)

    def get_error_response(self):
        return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=self.request.data)

        if not self.serializer.is_valid(raise_exception=True):
            return self.get_error_response()

        self.login()
        return self.get_response()


class LogoutView(APIView):
    """
    Calls logout method and delete the Token object
    assigned to the current User object.

    Accepts/Returns nothing.
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass

        logout(request)

        return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)


class UserDetailsView(RetrieveUpdateAPIView):
    """
    Returns User's details in JSON format.

    Accepts the following GET parameters: token
    Accepts the following POST parameters:
        Required: token
        Optional: email, first_name, last_name and UserProfile fields
    Returns the updated UserProfile and/or User object.
    """
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


"""
Calls Django Auth PasswordResetForm save method.

Accepts the following POST parameters: mobile
Returns the success/fail message.
"""


class PasswordResetView(GenericAPIView):
    '''
    请使用下面的正则表达式验证手机号码正确性，在提交服务器前客户端提交一次
    手机号码验证正则表达式：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
    '''
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')

        user = get_user_model().objects.filter(mobile=mobile)

        if not user:
            return Response({'errors': {'msgs': u'手机号码不存在', 'code': 400}}, status=status.HTTP_400_BAD_REQUEST)

        verify = send_verify_code(mobile)

        if not verify[0]:
            return Response({'errors': {'msgs': verify[1], 'code': 400}}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': u'验证码已经成功发送'}, status=status.HTTP_200_OK)

        # def post(self, request, *args, **kwargs):
        #     serializer = self.get_serializer(data=request.data)
        #
        #     if not serializer.is_valid():
        #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        #     serializer.save()
        #     # Return the success message with OK HTTP status
        #     return Response({"success": "Password reset e-mail has been sent."}, status=status.HTTP_200_OK)


"""
Password reset e-mail link is confirmed, therefore this resets the user's password.

Accepts the following POST parameters: new_password1, new_password2
Accepts the following Django URL arguments: token, uid
Returns the success/fail message.
"""


class PasswordResetConfirmView(GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"success": "Password has been reset with the new password."})


"""
Calls Django Auth SetPasswordForm save method.

Accepts the following POST parameters: new_password1, new_password2
Returns the success/fail message.
"""


class PasswordChangeView(GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"success": "New password has been saved."})

# class SocialLoginView(LoginView):
#     """
#     class used for social authentications
#     example usage for facebook with access_token
#     -------------
#     from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
#
#     class FacebookLogin(SocialLoginView):
#         adapter_class = FacebookOAuth2Adapter
#     -------------
#
#     example usage for facebook with code
#
#     -------------
#     from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
#     from allauth.socialaccount.providers.oauth2.client import OAuth2Client
#
#     class FacebookLogin(SocialLoginView):
#         adapter_class = FacebookOAuth2Adapter
#          client_class = OAuth2Client
#          callback_url = 'localhost:8000'
#     -------------
#     """
#
#     serializer_class = SocialLoginSerializer


# class SocialWeiboLogin(SocialLoginView):
#     adapter_class = WeiboOAuth2Adapter
