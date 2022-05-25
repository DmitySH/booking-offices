from djoser import email
from djoser.views import UserViewSet
from rest_framework import generics
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .. import serializers
from ..services import base_auth


class TokenAuthView(generics.GenericAPIView):
    """
    Token auth confirmation.
    """

    serializer_class = serializers.TokenAuthenticateSerializer

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = base_auth.validate_credentials(serializer.data)
            if user:
                if not user.is_active:
                    raise AuthenticationFailed(code=403,
                                               detail='Account is not activated')
                return Response(data=base_auth.create_token(user.id),
                                status=status.HTTP_200_OK)
            raise AuthenticationFailed(code=403,
                                       detail='No user with such credentials')

        else:
            raise AuthenticationFailed(code=403, detail='Bad auth data')


class ActivateUser(UserViewSet):
    """
    Activates user account.
    """

    def get_serializer(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            return None

        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        kwargs['data'] = {'uid': self.kwargs['uid'],
                          'token': self.kwargs['token']}

        return serializer_class(*args, **kwargs)

    def activation(self, request, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data='Successfully activated')


class ActivationEmail(email.ActivationEmail):
    template_name = 'accounts/activation.html'
