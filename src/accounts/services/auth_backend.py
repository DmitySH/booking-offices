import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication, exceptions

User = get_user_model()


class AuthBackend(authentication.BaseAuthentication):
    """
    Custom backend to auth via custom JWT.
    """

    authentication_header_prefix = 'Token'

    def authenticate(self, request, token=None, **kwargs):
        auth_header = authentication.get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower() != b'token':
            return None

        if len(auth_header) <= 1:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. No token.')
        elif len(auth_header) > 2:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. Too much spaces in token.')

        try:
            token = auth_header[1].decode('utf-8')
        except UnicodeError:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. Invalid chars in token.'
            )
        return self.authenticate_credential(token)

    @staticmethod
    def authenticate_credential(token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY,
                                 algorithms=settings.ALGORITHM)
        except jwt.PyJWTError as ex:
            if str(ex) == 'Signature has expired':
                raise exceptions.AuthenticationFailed(
                    'Signature has expired')
            raise exceptions.AuthenticationFailed(
                'Invalid auth. Can not decode token.')

        try:
            user = User.objects.get(id=payload['user_id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                'No user matching this token.')

        return user, None
