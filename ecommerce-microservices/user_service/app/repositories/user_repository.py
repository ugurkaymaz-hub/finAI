 # Kullanıcı verisiyle ilgili işlemleri burada yaparız (veritabanı)
from sqlalchemy.orm import Session , joinedload
from sqlalchemy.exc import NoResultFound
from app.models.user import User
from app.core.database import SessionLocal
from app.core.security import hash_password, verify_password
from fastapi import HTTPException, status

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self):
        return self.db.query(User).all()

    def get_user_details(self, username: str, load_role: bool = False) -> User | None:
        query = self.db.query(User).filter(User.username == username)
        if load_role:
            query = query.options(joinedload(User.role))
        return query.first()

    def save_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, username: str, user_data: User):
        user = self.get_user_details(username)
        for attr, value in user_data.dict().items():
            setattr(user, attr, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, username: str):
        user = self.get_user_details(username)
        self.db.delete(user)
        self.db.commit()
        return {"detail": "User deleted"}

    def change_password(self, username: str, old_password: str, new_password: str):
        user = self.get_user_details(username)
        if not verify_password(old_password, user.password):
            raise HTTPException(status_code=400, detail="Old password is incorrect")
        user.password = hash_password(new_password)
        self.db.commit()
        return {"detail": "Password updated successfully"}

    def reset_password(self, username: str):
        user = self.get_user_details(username)
        # Basit reset — production için değil
        user.password = hash_password("default123")
        self.db.commit()
        return {"detail": "Password reset to default123"}

    def deactivate_user(self, username: str):
        user = self.get_user_details(username)
        user.is_active = False
        self.db.commit()
        return {"detail": f"User {username} deactivated"}

    def deactivate_own_account(self, user: User):
        db_user = self.get_user_details(user.username)
        db_user.is_active = False
        self.db.commit()
        return {"detail": "Your account has been deactivated"}
