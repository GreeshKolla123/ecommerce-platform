from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.models import User
from app.schemas import User as UserSchema
from app.utils import get_user, get_user_by_username

router = APIRouter()

@router.post('/register')
def register(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_username(form_data.username)
    if user:
        return {'error': 'User already exists'}
    user = User(username=form_data.username, email=form_data.username, password=form_data.password)
    db.session.add(user)
    db.session.commit()
    return {'token': ' dummy token'}