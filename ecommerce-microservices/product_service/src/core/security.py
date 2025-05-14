#Library imports
from jose import jwt, JWTError

#Local imports
from src.core.config import settings

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
        return {
            "user_id": payload.get("user_id"),
            "role": payload.get("role"),
            "permissions": payload.get("permissions", [])
        }
    except JWTError:
        return None