 # JWT doğrulama ve rol kontrolü burada yapılır

from fastapi import Depends, HTTPException, status
from app.models.user import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError , jwt
from app.core.security import verify_access_token
from app.repositories.user_repository import UserRepository


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token") 


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


def is_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Yalnızca admin erişebilir"
        )
    return current_user

def is_user(current_user: User = Depends(get_current_user)):
    if current_user.role != "user":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Yalnızca kullanıcı erişebilir"
        )
    return current_user


