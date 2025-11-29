from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.config import settings
from app.models import User
from app.utils import get_password_hash, verify_password
from app.database import engine

auth_router = APIRouter()

@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User.query.filter_by(username=form_data.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = generate_token(user)
    return JSONResponse(content={"access_token": access_token, "token_type": "bearer"}, media_type="application/json")

@auth_router.post("/register")
def register(user: User):
    user.password = get_password_hash(user.password)
    db.session.add(user)
    db.session.commit()
    return JSONResponse(content={"message": "User created successfully"}, media_type="application/json")