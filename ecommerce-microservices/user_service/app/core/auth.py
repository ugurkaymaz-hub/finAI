 # JWT doğrulama ve rol kontrolü burada yapılır

from fastapi import Depends, HTTPException, status
from app.models.user import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError , jwt
from app.core.security import decode_access_token
from app.repositories.user_repository import UserRepository
from app.core.database import get_db 
from sqlalchemy.orm import Session



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token") 

# Kullanıcıyı token üzerinden almak

def get_current_user(token: str = Depends(oauth2_scheme) , db: Session = Depends(get_db)) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    user = UserRepository(db).get_user_details(username, load_role=True)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def is_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Yalnızca admin erişebilir"
        )
    return current_user



