from app.repositories.auth_repository import AuthRepository
from app.core.security import verify_password, create_access_token
from app.models.user import User
from datetime import timedelta
from fastapi import HTTPException
from app.schemas.auth_schema import LoginRequest, Token


class AuthService:

    @staticmethod
    def login(request: LoginRequest) -> Token:
        """Kullanıcıyı doğrular ve giriş için token döner."""
        user = AuthRepository.get_user_by_username(request.username)
        # Kullanıcı adı ve şifre kontrolü
        # Eğer kullanıcı yoksa veya şifre yanlışsa hata fırlatılır
        if not user or not verify_password(request.password, user.password): 
            raise HTTPException(status_code=401, detail="Invalid credentials")
        #Giriş yapan kullanıcı için token oluşturulur.
        token = create_access_token(data={"sub": user.username})
        return Token(access_token=token, token_type="bearer")

    @staticmethod
    def logout(token: str) -> bool:
        """Token'ı geçersiz kılar."""
        return AuthRepository.invalidate_token(token)

    @staticmethod
    def check_token_validity(token: str) -> bool:
        """Token geçerliliğini kontrol eder."""
        user = AuthRepository.get_user_from_token(token)
        if user is None:
            return False
        return True