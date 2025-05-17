# Tüm kullanıcı işlemlerini burada tanımlayacağız

from fastapi import APIRouter, Depends , Security
from app.schemas.user_schema import UserCreate , UserUpdate , UserPasswordChangeRequest , UserResponse , UserDeleteResponse , UserCreateResponse , UserDeactivateResponse , UserChangePasswordResponse
from app.services.user_services import UserService
from app.models.user import User
from app.core.auth import is_admin , get_current_user
from app.schemas.user_schema import UserBase
from app.controllers.auth_controller import oauth2_scheme
from app.core.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/users", tags=["Users"])

user_service = UserService()


# Kullanıcıları getir (Admin)
@router.get("/user" ,  response_model=list[UserResponse])
async def get_users(user: User = Depends(is_admin)):
    return user_service.get_all_users()


# Kullanıcı detayı getir (Admin)
@router.get("/user/{username}" , response_model=UserResponse)
async def get_user_details(username: str, user: User = Depends(is_admin)):
    return user_service.get_user_details(username)


# Yeni kullanıcı oluştur.
@router.post("/user" ,  response_model=UserCreateResponse)
async def create_user(user_data: UserCreate , db: Session = Depends(get_db)):
    created_user = user_service.create_user(user_data , db) 
    return UserCreateResponse(
        message="User created successfully",
        created_user=UserResponse.from_orm(created_user)
    )


# Kullanıcıyı güncelle (Admin)
@router.put("/user/{username}" , response_model=UserResponse)
async def update_user(username: str, user_data: UserUpdate, user: User = Depends(is_admin)):
    return user_service.update_user(username, user_data)


# Kullanıcıyı sil (soft delete) (Admin)
@router.delete("/user/{username}" , response_model=UserDeleteResponse)
async def delete_user(username: str, user: User = Depends(is_admin)):
    return user_service.delete_user(username)


# Şifre değiştir (User)
@router.put("/user/{username}/change-password" , response_model=UserChangePasswordResponse)
async def change_password(username: str, passwords: UserPasswordChangeRequest):
    return user_service.change_password(username, passwords.old_password, passwords.new_password)


# Şifre sıfırla (Admin)
@router.put("/user/{username}/reset-password")
async def reset_password(username: str, user: User = Depends(is_admin)):
    return user_service.reset_password(username)

# Kendi bilgilerini getir (User, Admin)
@router.get("/user/me" , response_model=UserResponse)
async def get_my_info(user: User = Depends(get_current_user)):
    return user_service.get_my_info(user)


# Başka kullanıcıyı pasifleştir (Admin)
@router.put("/user/{username}/deactivate" , response_model=UserDeactivateResponse)
async def deactivate_user(username: str, user: User = Depends(is_admin)):
    return user_service.deactivate_user(username)


# Kendi hesabını pasifleştir (User)
@router.put("/user/me/deactivate" , response_model=UserDeactivateResponse)
async def deactivate_own_account(user: User = Depends(is_admin)):
    return user_service.deactivate_own_account(user)


