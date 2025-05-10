from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from app.utils.jwt_utils import decode_jwt
import jwt


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Sadece belirli endpointlerde doğrulama isteyebiliriz.
        
        authorization: str = request.headers.get("Authorization")

        if authorization is None or not authorization.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Authorization token missing or invalid"})

        token = authorization.split(" ")[1]

        try:
            payload = decode_jwt(token)
            request.state.user = payload  # Örn: {"user_id": 1, "role": "admin"}
        except jwt.ExpiredSignatureError:
            return JSONResponse(status_code=401, content={"detail": "Token has expired"})
        except jwt.InvalidTokenError:
            return JSONResponse(status_code=401, content={"detail": "Invalid token"})

        response = await call_next(request)
        return response