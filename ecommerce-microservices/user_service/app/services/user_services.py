# Kullanıcı işlemlerinin iş mantığını burada tanımlarız

from app.schemas.user_schema import UserCreate , UserPasswordChangeRequest
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password 
from fastapi import HTTPException
from app.models.user import User

class UserService:

    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_details(username: str):
        return UserRepository.get_user_details(username)

    @staticmethod
    def create_user(user_data: UserCreate):
        # Şifreyi hash'le
        hashed_password = hash_password(user_data.password)
        # Yeni kullanıcıyı oluştur ve kaydet
        user = User(
            username=user_data.username, 
            password=hashed_password , 
            full_name=user_data.full_name ,
            is_active=user_data.is_active
        )
        return UserRepository.save_user(user)
    
    @staticmethod
    def delete_user(username: str):
        return UserRepository.delete_user(username)

    @staticmethod
    def update_user(username: str, user_data: User):
        return UserRepository.update_user(username, user_data)

    
    @staticmethod
    def change_password(username: str, passwords: UserPasswordChangeRequest):
        # Burada eski şifre doğrulama ve yeni şifre hash'leme işlemi ekleyebilirsiniz
        return UserRepository.change_password(username, passwords.old_password, passwords.new_password)

    @staticmethod
    def reset_password(username: str):
        return UserRepository.reset_password(username)

    @staticmethod
    def get_my_info(user: User):
        return user  # Kullanıcı bilgilerini döndürüyoruz

    @staticmethod
    def deactivate_user(username: str):
        return UserRepository.deactivate_user(username)

    @staticmethod
    def deactivate_own_account(user: User):
        return UserRepository.deactivate_own_account(user)