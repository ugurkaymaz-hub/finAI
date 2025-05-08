 # JWT doğrulama ve rol kontrolü burada yapılır

from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.core.security import get_current_user  # JWT token'dan kullanıcıyı çözüyorsa

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