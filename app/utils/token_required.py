import jwt
from flask import request

from app.respsonses import token_not_found, token_invalid
from config import DevelopmentConfig


def token_required(function):
    def wrap(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return token_not_found()

        try:
            data = jwt.decode(token, DevelopmentConfig.SECRET_KEY)
        except:
            return token_invalid()

        return function(*args, **kwargs)

    wrap.__name__ = function.__name__
    return wrap
