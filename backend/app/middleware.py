from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def authenticate_request(request: Request):
    try:
        token = request.headers['Authorization'].split(' ')[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload['sub']
    except JWTError:
        return None
    except IndexError:
        return None