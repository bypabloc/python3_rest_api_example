import jwt
import os
import datetime
import time
from django.utils.timezone import now
from ..models import Session
from dotenv import load_dotenv
load_dotenv()
    
JWT_SECRET_KEY_PRIVATE = os.getenv('JWT_SECRET_KEY_PRIVATE')

print('JWT_SECRET_KEY_PRIVATE',JWT_SECRET_KEY_PRIVATE)

def timeExpired():
    expirationInSeconds = 60 * 60; # one hour
    dateTokenExpiration = datetime.datetime.now() + datetime.timedelta(seconds=expirationInSeconds)

    # dateTokenExpiration 2021-11-30 01:30:35.306659
    # dateTokenExpiration 2021-11-30 02:30:50.513881 
    # dateTokenExpiration.strftime('%Y-%m-%d %H:%M:%S') 2021-11-30 01:30:35
    
    return {
        'expirationInSeconds': expirationInSeconds,
        'dateTokenExpiration': dateTokenExpiration,
    }

def generateToken(uuid, user_id):
    print('generateToken')
    print('uuid',uuid)
    print('user_id',user_id)
    print('JWT_SECRET_KEY_PRIVATE',JWT_SECRET_KEY_PRIVATE)
    
    expirationInSeconds, dateTokenExpiration = timeExpired().values()
    print('expirationInSeconds',expirationInSeconds)
    print('dateTokenExpiration',dateTokenExpiration)

    jwt_payload = jwt.encode(
        {
            # "exp": dateTokenExpiration,
            "exp": datetime.datetime.now() + datetime.timedelta(seconds=0),
        },
        JWT_SECRET_KEY_PRIVATE,
        algorithm="HS256",
    )

    destroyTokens(user_id=user_id);

    session = Session.objects.create(
        token=jwt_payload,
        user_id=user_id,
        expired_at=dateTokenExpiration,
    )

    return session

def existsToken(token):
    print('existsToken')
    print('token',token)

    session = Session.objects.filter(token=token)
    if session.exists():
        return session.first()
    else:
        return False

def verifyToken(token):
    print('verifyToken')
    print('token',token)

    Session = existsToken(token);
    if Session:
        if Session.expired_at > now():
            return Session
        else:
            destroyTokens(user_id=Session.user_id)

    refreshToken(session=Session);

    return Session

def refreshToken(session):
    print('refreshToken')
    print('session',session)

    dateTokenExpiration = timeExpired();
    
    session.update(expired_at=dateTokenExpiration)

    return True

def destroyTokens(user_id):
    print('destroyTokens')
    print('user_id',user_id)
    
    Session.objects.filter(user_id=user_id).delete()

    return True