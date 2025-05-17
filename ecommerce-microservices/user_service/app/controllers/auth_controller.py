from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.schemas.auth_schema import LoginRequest, Token
from app.services.auth_service import AuthService
from app.core.auth import get_current_user

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Giriş Yap
@router.post("/login", response_model=Token)
def login(request: LoginRequest):
    """Kullanıcı girişini yapar ve token döner."""
    return AuthService.login(request)

# Oturum Kapat
@router.post("/logout" , response_model=dict)
def logout(token: str = Depends(oauth2_scheme)):
    """Giriş yapan kullanıcının oturumunu kapatır."""
    success = AuthService.logout(token)
    if not success:
        raise HTTPException(status_code=400, detail="Logout failed")
    return {"msg": "User logged out successfully"}

# Token Geçerliliği Kontrolü
@router.get("/checkLogin")
def check_login(token: str = Depends(oauth2_scheme)):
    """Token'ın geçerliliğini kontrol eder."""
    valid = AuthService.check_token_validity(token)
    if not valid:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"msg": "Token is valid"}