from datetime import timedelta, datetime

import jwt
from django.conf import settings
from django.contrib.auth import authenticate


def validate_credentials(credentials):
    user = authenticate(**credentials)
    return user


def create_token(user_id):
    """
    Creates token.
    """

    token_expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        'user_id': user_id,
        'access_token': create_access_token(
            data={'user_id': user_id}, expires_delta=token_expire
        ),
        'token_type': 'Token'
    }


def create_access_token(data, expires_delta=None):
    to_encode = data.copy()
    if expires_delta is not None:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire, 'sub': 'access'})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY,
                             algorithm=settings.ALGORITHM)

    return encoded_jwt
