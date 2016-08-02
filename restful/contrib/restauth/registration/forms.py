# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import unicodedata

# from allauth.account.forms import SetPasswordField
from django.conf import settings

from .adapter import get_adapter
from .utils import user_email, user_field, user_username
from django import forms
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError

from .. import app_settings


class PasswordField(forms.CharField):
    def __init__(self, *args, **kwargs):
        render_value = kwargs.pop('render_value', False)
        kwargs['widget'] = forms.PasswordInput(render_value=render_value,
            attrs={'placeholder':
                _(kwargs.get("label"))})
        super(PasswordField, self).__init__(*args, **kwargs)


class SetPasswordField(PasswordField):
    def clean(self, value):
        value = super(SetPasswordField, self).clean(value)
        value = get_adapter().clean_password(value)
        return value


class SignupForm(forms.Form):
    mobile = forms.CharField(label=_(u"手机号"), max_length=20, required=True)
    verify = forms.CharField(label=_(u"验证码"), max_length=10, required=False)
    device = forms.CharField(label=_(u"设备号"), max_length=200, required=True)

    password1 = SetPasswordField(label=_(u"登陆密码"), required=True)
    password2 = PasswordField(label=_(u"确认密码"), required=True)

    jpush_registration_id = forms.CharField(label=_(u"jpush_registration_id"), max_length=200, required=False)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        if not app_settings.SIGNUP_PASSWORD_VERIFICATION:
            del self.fields["password2"]

    def clean(self):
        super(forms.Form, self).clean()

        if not self.cleaned_data.get("mobile", None):
            raise ValidationError({'mobile': _("手机号码不能为空.")})

        if app_settings.SIGNUP_PASSWORD_VERIFICATION and "password1" in self.cleaned_data and "password2" in self.cleaned_data:
            if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
                raise ValidationError({'password': _("两次密码不一致.")})

        # if not self.cleaned_data.get("verify", None):
        #     raise ValidationError({'verify': _("验证码不能为空.")})

        # 判断验证码
        # verify_status, verify_message = check_verify_code(self.cleaned_data["mobile"], self.cleaned_data["verify"])
        #
        # if not verify_status:
        #     raise ValidationError({'verify': verify_message})

        if not self.cleaned_data.get("device", None):
            raise ValidationError({'device': _("设备号码不能为空.")})

        # 判断手机是否注册过
        if get_user_model()._default_manager.filter(mobile=self.cleaned_data['mobile']).exists():
            raise ValidationError(_("用户手机号码已经注册过."))

        return self.cleaned_data

    def save(self, request):
        user = get_user_model()()
        nums = get_user_model().objects.filter(device=self.cleaned_data.get("device")).count()
        print nums, user, self.cleaned_data.get("device")

        if nums >= settings.DEVICE_MAX_REG_NUMS:
            raise ValidationError(_("该设备超出最大注册数."))

        self.save_user(request, user, self)
        return user

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        data = form.cleaned_data

        mobile = data.get('mobile')
        verify = data.get('verify')
        device = data.get('device')
        jpush_registration_id = data.get('jpush_registration_id')

        if verify:
            user_field(user, 'verify', verify)

        if device:
            user_field(user, 'device', device)

        if mobile:
            user_field(user, 'mobile', mobile)

        if jpush_registration_id:
            user_field(user, 'jpush_registration_id', jpush_registration_id)

        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()

        self.populate_username(request, user)

        if commit:
            user.save()

        return user

    def populate_username(self, request, user):
        """
        Fills in a valid username, if required and missing.  If the
        username is already present it is assumed to be valid
        (unique).
        """
        # from .utils import user_username, user_email, user_field
        mobile = user_field(user, 'mobile')
        # last_name = user_field(user, 'last_name')
        email = user_email(user)
        username = user_username(user)

        # if app_app_settings.USER_MODEL_USERNAME_FIELD:
        user_username(user, username or self.generate_unique_username([mobile, email, 'user']))

    def generate_unique_username(self, txts, regex=None):
        return generate_unique_username(txts, regex)


def _generate_unique_username_base(txts, regex=None):
    username = None
    regex = regex or '[^\w\s@+.-]'
    for txt in txts:
        if not txt:
            continue
        username = unicodedata.normalize('NFKD', force_text(txt))
        username = username.encode('ascii', 'ignore').decode('ascii')
        username = force_text(re.sub(regex, '', username).lower())
        # Django allows for '@' in usernames in order to accomodate for
        # project wanting to use e-mail for username. In allauth we don't
        # use this, we already have a proper place for putting e-mail
        # addresses (EmailAddress), so let's not use the full e-mail
        # address and only take the part leading up to the '@'.
        username = username.split('@')[0]
        username = username.strip()
        username = re.sub('\s+', '_', username)
        if username:
            break
    return username or 'user'


def generate_unique_username(txts, regex=None):
    # from .account.app_settings import USER_MODEL_USERNAME_FIELD
    username = _generate_unique_username_base(txts, regex)
    User = get_user_model()
    max_length = 20
    i = 0
    while True:
        try:
            if i:
                pfx = str(i + 1)
            else:
                pfx = ''
            ret = username[0:max_length - len(pfx)] + pfx
            query = {'username' + '__iexact': ret}
            User.objects.get(**query)
            i += 1
        except User.DoesNotExist:
            return ret
