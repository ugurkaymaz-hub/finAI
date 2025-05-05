from app.models.user import User
from app.core.database import SessionLocal
from app.core.security import decode_access_token

class AuthRepository:

    @staticmethod
    def get_user_by_username(username: str) -> User:
        """Kullanıcıyı kullanıcı adıyla veritabanından alır."""
        db = SessionLocal()
        user = db.query(User).filter(User.username == username).first()
        db.close()
        return user

    @staticmethod
    def invalidate_token(token: str) -> bool:
        """Token geçersiz kılma işlemi yapılır."""
        # Bu örnek için basitçe token geçersiz kılma işlemi olmadığını varsayalım.
        # Gerçek dünyada, token’ları blacklistlemek için bir mekanizma gerekebilir.
        return True

    @staticmethod
    def get_user_from_token(token: str) -> User:
        """Token’dan kullanıcı bilgilerini alır."""
        try:
            user_data = decode_access_token(token)
            return user_data
        except:
            return None