 # Kullanıcı verisiyle ilgili işlemleri burada yaparız (veritabanı)

from app.core.database import SessionLocal
from app.models.user import User

class UserRepository:
    def __init__(self):
        self.db = SessionLocal()

    def save_user(self, user_data):
        user = User(**user_data.dict())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def __del__(self):
        self.db.close()