import jwt
import os
from ..models import Session
from dotenv import load_dotenv
load_dotenv()
    
JWT_SECRET_KEY_PRIVATE = os.getenv('JWT_SECRET_KEY_PRIVATE')

print('JWT_SECRET_KEY_PRIVATE',JWT_SECRET_KEY_PRIVATE)