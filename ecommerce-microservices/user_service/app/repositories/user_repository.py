 # Kullanıcı verisiyle ilgili işlemleri burada yaparız (veritabanı)

from app.core.database import SessionLocal
from app.models.user import User

def save_user(user_data):
    db = SessionLocal()
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user