# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from .serializers import LoginSerializer as DefaultLoginSerializer
from .serializers import \
    PasswordChangeSerializer as DefaultPasswordChangeSerializer
from .serializers import \
    PasswordResetConfirmSerializer as DefaultPasswordResetConfirmSerializer
from .serializers import \
    PasswordResetSerializer as DefaultPasswordResetSerializer
from .serializers import TokenSerializer as DefaultTokenSerializer
from .serializers import UserDetailsSerializer as DefaultUserDetailsSerializer
from .utils import import_callable

serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})

TokenSerializer = import_callable(
    serializers.get('TOKEN_SERIALIZER', DefaultTokenSerializer))

UserDetailsSerializer = import_callable(
    serializers.get('USER_DETAILS_SERIALIZER', DefaultUserDetailsSerializer)
)

LoginSerializer = import_callable(
    serializers.get('LOGIN_SERIALIZER', DefaultLoginSerializer)
)

PasswordResetSerializer = import_callable(
    serializers.get(
        'PASSWORD_RESET_SERIALIZER',
        DefaultPasswordResetSerializer
    )
)

PasswordResetConfirmSerializer = import_callable(
    serializers.get(
        'PASSWORD_RESET_CONFIRM_SERIALIZER',
        DefaultPasswordResetConfirmSerializer
    )
)

PasswordChangeSerializer = import_callable(
    serializers.get(
        'PASSWORD_CHANGE_SERIALIZER',
        DefaultPasswordChangeSerializer
    )
)
