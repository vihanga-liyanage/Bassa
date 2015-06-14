from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from UserManager import *

def generate_auth_token(user, key, expiration = 600):
        s = Serializer(key, expires_in = expiration)
        return s.dumps({ 'userName': user.userName})

def verify_auth_token(token, key):
    s = Serializer(key)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None # valid token, but expired
    except BadSignature:
        return None # invalid token
    user = get_user(data['userName'])
    return user
