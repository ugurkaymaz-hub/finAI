from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.core.auth import get_current_user
from fastapi.security import OAuth2PasswordBearer
from app.core.database import SessionLocal
from sqlalchemy.orm import Session
from core.config import settings
from app.repositories.user_repository import UserRepository
from typing import Optional



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token") 

#Burayı authentication yapısı için ekledik.Şifre doğrulama, token oluşturma ve doğrulama işlemleri burada yapılır.

SECRET_KEY = settings.JWT_SECRET_KEY  
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# JWT oluşturma
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Token'ı doğrulama
def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    
#Eski şifre ile şimdikini karşılaştırma
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Kullanıcıyı token üzerinden almak
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    user = UserRepository().get_user_details(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Admin rolünü kontrol et
def is_admin(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="You are not authorized to perform this action.")
    return current_user

# Kullanıcı rolünü kontrol et
def is_user(current_user: User = Depends(get_current_user)):
    if current_user.is_admin:  # Admin kullanıcılar da user olarak geçebilir
        raise HTTPException(status_code=403, detail="Admin users cannot perform this action.")
    return current_user
    








