from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from core.security import decode_jwt

auth_scheme = HTTPBearer()

def require_user(token: str = Depends(auth_scheme)):
    decoded = decode_jwt(token.credentials)
    if not decoded:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return decoded