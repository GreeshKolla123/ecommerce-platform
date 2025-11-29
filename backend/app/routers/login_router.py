from fastapi import APIRouter, Depends
from app.models import User
from app.schemas import UserLogin
from app.utils.auth import verify_password
from app.utils.db import get_db

login_router = APIRouter()

@login_router.post('/api/login')
def login(user: UserLogin, db: Session = Depends(get_db)):
    user_in = db.query(User).filter(User.username == user.username).first()
    if user_in and verify_password(user.password, user_in.password):
        return {'token': 'token'}
    return {'error': 'Invalid username or password'}
