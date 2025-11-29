from passlib.context import CryptContext
from jose import jwt

pwd_context = CryptContext(schemes=['bcrypt'], default='bcrypt')
secret_key = 'dev-secret-key-change-in-production'

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_current_user(token: str):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        user_id: int = payload.get('user_id')
        return user_id
    except:
        return None
