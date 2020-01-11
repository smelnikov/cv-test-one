from django.utils.translation import ugettext_lazy as _
from rest_framework import HTTP_HEADER_ENCODING, authentication, exceptions

from . import models


def get_api_key_header(request):
    """
    Возвращает HTTP заголовок 'ApiKey:'
    """
    auth = request.META.get('HTTP_APIKEY', b'')
    if isinstance(auth, str):
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


class ApiKeyUser(object):
    @property
    def is_authenticated(self):
        return True


class ApplicationAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth = get_api_key_header(request)
        if not auth:
            return None
        try:
            api_key = auth.decode()
        except UnicodeError:
            msg = _('Invalid ApiKey header. ApiKey string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(api_key)

    def authenticate_credentials(self, key):
        try:
            application = models.Application.objects.get(key=key)
        except application.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid ApiKey.'))

        return ApiKeyUser(), application

    def authenticate_header(self, request):
        return 'ApiKey'
