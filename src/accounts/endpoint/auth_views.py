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
                return Response(data=base_auth.create_token(user.id),
                                status=status.HTTP_200_OK)
            raise AuthenticationFailed(code=403,
                                       detail='No user with such credentials')

        else:
            raise AuthenticationFailed(code=403, detail='Bad auth data')
