from jose import jwt, JWTError
from core.config import JWT_SECRET_KEY

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        return {
            "user_id": payload.get("user_id"),
            "role": payload.get("role"),
            "permissions": payload.get("permissions", [])
        }
    except JWTError:
        return None