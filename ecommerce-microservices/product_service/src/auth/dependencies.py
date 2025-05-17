from fastapi import Depends, HTTPException, Header, status
from jose import JWTError, jwt
from typing import Optional, Dict

#Local imports

from src.core.config import Settings

settings = Settings()

def decode_jwt_token(token: str) -> Dict:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return {
            "user_id": payload.get("sub"),
            "role": payload.get("role"),
            "permissions": payload.get("permissions", [])
        }
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Geçersiz kimlik doğrulama bilgisi",
        )


def get_current_user(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Kimlik doğrulama başlığı eksik"
        )
    token = authorization.split(" ")[1]
    user = decode_jwt_token(token)
    return user


def require_admin(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Yönetici yetkisi gerekli"
        )
    return user


def require_user(user: dict = Depends(get_current_user)):
    # Kullanıcı doğrulama işlemi: kullanıcı geçerli ve kimlik doğrulaması yapılmış mı kontrol eder
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Kimlik doğrulama başarısız"
        )
    return user
