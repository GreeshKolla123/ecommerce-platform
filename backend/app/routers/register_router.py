from fastapi import APIRouter, Depends
from app.models import User
from app.schemas import UserCreate
from app.utils.auth import get_password_hash, verify_password
from app.utils.db import get_db

register_router = APIRouter()

@register_router.post('/api/register')
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    user_in = User(username=user.username, email=user.email, password=hashed_password)
    db.add(user_in)
    db.commit()
    return {'token': 'token'}
