from __future__ import absolute_import

import datetime
import random
from hashlib import md5 as _md5
from hashlib import sha1 as _sha1

from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlencode
from django.utils.six import text_type

from .compat import SiteProfileNotAvailable, get_model
from .models import Settings
from .models import UserProfile as Profile

md5 = lambda x: _md5(force_bytes(x, errors='replace'))
sha1 = lambda x: _sha1(force_bytes(x, errors='replace'))

try:
    from django.utils.text import truncate_words
except ImportError:
    from django.utils.text import Truncator
    from django.utils.functional import allow_lazy


    def truncate_words(s, num, end_text='...'):
        truncate = end_text and ' %s' % end_text or ''
        return Truncator(s).words(num, truncate=truncate)


    truncate_words = allow_lazy(truncate_words, text_type)


def upload_to_mugshot(instance, filename):
    """
    Uploads a mugshot for a user to the ``USERENA_MUGSHOT_PATH`` and saving it
    under unique hash for the image. This is for privacy reasons so others
    can't just browse through the mugshot directory.

    """

    extension = filename.split('.')[-1].lower()
    salt, hash = generate_sha1(instance.pk)

    path = settings.USERENA_MUGSHOT_PATH % {
        'date_now': get_datetime_now().date(),
        'username': instance.user.username,
        'date': instance.user.date_joined,
        'id': instance.user.id,
    }

    # fs = HashFS(filename, depth=4, width=1, algorithm='md5')
    # fp = fs.put(filename, '.%s' % extension)

    return '%(path)s%(hash)s.%(extension)s' % {
        'path': path,
        'hash': hash[:10],
        'extension': extension
    }


def get_gravatar(email, size=80, default='identicon'):
    """ Get's a Gravatar for a email address.

    :param size:
        The size in pixels of one side of the Gravatar's square image.
        Optional, if not supplied will default to ``80``.

    :param default:
        Defines what should be displayed if no image is found for this user.
        Optional argument which defaults to ``identicon``. The argument can be
        a URI to an image or one of the following options:

            ``404``
                Do not load any image if none is associated with the email
                hash, instead return an HTTP 404 (File Not Found) response.

            ``mm``
                Mystery-man, a simple, cartoon-style silhouetted outline of a
                person (does not vary by email hash).

            ``identicon``
                A geometric pattern based on an email hash.

            ``monsterid``
                A generated 'monster' with different colors, faces, etc.

            ``wavatar``
                Generated faces with differing features and backgrounds

    :return: The URI pointing to the Gravatar.

    """
    if settings.USERENA_MUGSHOT_GRAVATAR_SECURE:
        base_url = 'https://secure.gravatar.com/avatar/'
    else:
        base_url = '//www.gravatar.com/avatar/'

    gravatar_url = '%(base_url)s%(gravatar_id)s?' % \
                   {'base_url': base_url,
                       'gravatar_id': md5(email.lower().encode('utf-8')).hexdigest()}

    gravatar_url += urlencode({'s': str(size), 'd': default})

    return gravatar_url


def generate_sha1(string, salt=None):
    """
    Generates a sha1 hash for supplied string. Doesn't need to be very secure
    because it's not used for password checking. We got Django for that.

    :param string:
        The string that needs to be encrypted.

    :param salt:
        Optionally define your own salt. If none is supplied, will use a random
        string of 5 characters.

    :return: Tuple containing the salt and hash.

    """
    if not isinstance(string, (str, text_type)):
        string = str(string)

    if not salt:
        salt = sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]

    salted_bytes = (salt.encode('utf-8') + string.encode('utf-8'))
    hash_ = sha1(salted_bytes).hexdigest()

    return salt, hash_


def get_settings_model():
    """
    Return the model class for the currently-active user profile
    model, as defined by the ``AUTH_PROFILE_MODULE`` setting.

    :return: The model that is used as profile.

    """
    if (not hasattr(settings, 'AUTH_PROFILE_MODULE')) or (not settings.AUTH_PROFILE_MODULE):
        raise SiteProfileNotAvailable

    try:
        settings_mod = get_model(*settings.AUTH_SETTINGS_MODULE.rsplit('.', 1))
    except LookupError:
        settings_mod = None

    if settings_mod is None:
        raise SiteProfileNotAvailable

    return settings_mod


def get_profile_model():
    """
    Return the model class for the currently-active user profile
    model, as defined by the ``AUTH_PROFILE_MODULE`` setting.

    :return: The model that is used as profile.

    """
    if (not hasattr(settings, 'AUTH_PROFILE_MODULE')) or (not settings.AUTH_PROFILE_MODULE):
        raise SiteProfileNotAvailable

    try:
        profile_mod = get_model(*settings.AUTH_PROFILE_MODULE.rsplit('.', 1))
    except LookupError:
        profile_mod = None

    if profile_mod is None:
        raise SiteProfileNotAvailable

    return profile_mod


def get_user_settings(user):
    settings_model = Settings

    try:
        settings = user.get_settings()
    except AttributeError:
        related_name = settings_model._meta.get_field_by_name('owner')[0].related_query_name()
        settings = getattr(user, related_name, None)
    except settings_model.DoesNotExist:
        settings = None

    if settings:
        return settings

    return settings_model.objects.create(owner=user)


def get_user_profile(user):
    # profile_model = get_profile_model()
    profile_model = Profile

    try:
        profile = user.get_profile()
    except AttributeError:
        related_name = profile_model._meta.get_field_by_name('owner')[0].related_query_name()
        profile = getattr(user, related_name, None)
    except profile_model.DoesNotExist:
        profile = None

    if profile:
        return profile

    return profile_model.objects.create(owner=user)


def get_protocol():
    """
    Returns a string with the current protocol.

    This can be either 'http' or 'https' depending on ``USERENA_USE_HTTPS``
    setting.

    """
    protocol = 'http'

    if getattr(settings, 'USERENA_USE_HTTPS', settings.DEFAULT_USERENA_USE_HTTPS):
        protocol = 'https'

    return protocol


def get_datetime_now():
    """
    Returns datetime object with current point in time.

    In Django 1.4+ it uses Django's django.utils.timezone.now() which returns
    an aware or naive datetime that represents the current point in time
    when ``USE_TZ`` in project's settings is True or False respectively.
    In older versions of Django it uses datetime.datetime.now().

    """
    try:
        from django.utils import timezone
        return timezone.now()  # pragma: no cover
    except ImportError:  # pragma: no cover
        return datetime.datetime.now()
