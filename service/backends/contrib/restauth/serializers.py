# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from restful.helpers import check_verify_code
from .forms import PasswordResetForm


class VerifyMobileSerializer(serializers.Serializer):
    mobile = serializers.CharField(required=False, allow_blank=True)


class RegisterSerializer(serializers.Serializer):
    mobile = serializers.CharField(label=_(u'手机号'), required=True, allow_blank=True)

    password1 = serializers.CharField(label=_(u'登录密码'), style={'input_type': 'password'})
    password2 = serializers.CharField(label=_(u'确认密码'), style={'input_type': 'password'})

    verify = serializers.CharField(label=_(u'验证码'), required=True, allow_blank=True)
    device = serializers.CharField(label=_(u'设备号'), required=True, allow_blank=True, help_text=_('隐藏字段,设备自动获取'))

    jpush_registration_id = serializers.CharField(style={'input_type': 'text'}, required=False,
        label=u'jpush_registration_id', help_text=_('极光推送的registration_id'))


class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(required=False, allow_blank=True, label=u'手机号码')
    password = serializers.CharField(style={'input_type': 'password'}, label=u'登录密码')
    jpush_registration_id = serializers.CharField(style={'input_type': 'text'}, required=False,
        label=u'jpush_registration_id')

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        mobile = attrs.get('mobile')

        if mobile and password:
            user = authenticate(mobile=mobile, password=password)
        elif username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = _('必须包含 "username" 和 "password".')
            raise ValidationError(msg)

        if user:
            if not user.is_active:
                raise ValidationError(_('用户帐户被禁用.'))
        else:
            raise ValidationError(_('手机号或密码错误,无法登录.'))

        attrs['user'] = user
        return attrs


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = Token
        fields = ('key',)


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    class Meta:
        model = get_user_model()
        # fields = ('username', 'email', 'first_name', 'last_name')
        # read_only_fields = ('email',)


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """

    mobile = serializers.CharField()
    password_reset_form_class = PasswordResetForm

    def validate_mobile(self, value):
        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)

        if not self.reset_form.is_valid():
            raise serializers.ValidationError('Error')

        return value

    def save(self):
        request = self.context.get('request')
        # user = get_user_model()
        # if user.mobile == self.mobile:

        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'request': request,
        }
        self.reset_form.save(**opts)


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """

    mobile = serializers.CharField(required=True)
    verify = serializers.CharField(required=True)

    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    def validate(self, attrs):
        self._errors = {}

        # Get the UserModel
        UserModel = get_user_model()

        # Decode the uidb64 to uid to get User object
        try:
            user = UserModel.objects.filter(mobile=attrs['mobile']).get()

            if user:
                # Construct SetPasswordForm instance
                self.set_password_form = self.set_password_form_class(user=user, data=attrs)
            else:
                raise exceptions.ValidationError({'mobile': [u'手机号码不存在']})
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise exceptions.ValidationError({'mobile': [u'手机号码不存在']})

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        verify = check_verify_code(attrs['mobile'], attrs['verify'])

        if not verify[0]:
            raise exceptions.ValidationError({'detail': verify[1]})

        return attrs

    def save(self):
        self.set_password_form.save()


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        self.old_password_field_enabled = getattr(settings, 'OLD_PASSWORD_FIELD_ENABLED', False)
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        if not self.old_password_field_enabled:
            self.fields.pop('old_password')

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

    def validate_old_password(self, value):
        invalid_password_conditions = (
            self.old_password_field_enabled,
            self.user,
            not self.user.check_password(value)
        )

        if all(invalid_password_conditions):
            raise serializers.ValidationError('Invalid password')

        return value

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(user=self.user, data=attrs)

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        return attrs

    def save(self):
        self.set_password_form.save()
