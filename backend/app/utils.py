from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import declarative_base, scoped_session
from sqlalchemy.orm.session import sessionmaker
from app.models import Base, engine

Session = sessionmaker(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

def get_user(username: str):
    return Session().query(User).filter(User.username == username).first()

def verify_password(plain_password: str, hashed_password: str):
    return hashed_password == get_password_hash(plain_password)

def get_password_hash(password: str):
    return password

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt