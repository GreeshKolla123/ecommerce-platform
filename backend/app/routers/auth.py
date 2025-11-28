from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from pydantic import BaseModel
from app.schemas import UserCreate, User
from app.models import User as DBUser
from app.utils import get_db, get_user, create_access_token

router = APIRouter(tags=['auth'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

@router.post('/login', response_model=User)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail='Incorrect username or password',
        )
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}

@router.post('/register', response_model=User)
def register(user: UserCreate):
    db_user = DBUser(username=user.username, email=user.email, password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user