# Tüm kullanıcı işlemlerini burada tanımlayacağız

from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserCreate
from app.services.user_services import create_user
from app.services.user_services import UserService
from app.models.user import User
from app.core.auth import is_admin, is_user


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def register_user(user: UserCreate):
    return create_user(user)


router = APIRouter()

# Kullanıcıları getir (Admin)
@router.get("/user")
async def get_users(user: User = Depends(is_admin)):
    return UserService.get_all_users()

# Kullanıcı detayı getir (Admin)
@router.get("/user/{username}")
async def get_user_details(username: str, user: User = Depends(is_admin)):
    return UserService.get_user_details(username)

# Yeni kullanıcı oluştur (Admin)
@router.post("/user")
async def create_user(user_data: User, user: User = Depends(is_admin)):
    return UserService.create_user(user_data)

# Kullanıcıyı güncelle (Admin)
@router.put("/user/{username}")
async def update_user(username: str, user_data: User, user: User = Depends(is_admin)):
    return UserService.update_user(username, user_data)

# Kullanıcıyı sil (soft delete) (Admin)
@router.delete("/user/{username}")
async def delete_user(username: str, user: User = Depends(is_admin)):
    return UserService.delete_user(username)

# Şifre değiştir (User)
@router.put("/user/{username}/change-password")
async def change_password(username: str, old_password: str, new_password: str, user: User = Depends(is_user)):
    return UserService.change_password(username, old_password, new_password)

# Şifre sıfırla (Admin)
@router.put("/user/{username}/reset-password")
async def reset_password(username: str, user: User = Depends(is_admin)):
    return UserService.reset_password(username)

# Kendi bilgilerini getir (User, Admin)
@router.get("/user/me")
async def get_my_info(user: User = Depends(is_user)):
    return UserService.get_my_info(user)

# Başka kullanıcıyı pasifleştir (Admin)
@router.put("/user/{username}/deactivate")
async def deactivate_user(username: str, user: User = Depends(is_admin)):
    return UserService.deactivate_user(username)

# Kendi hesabını pasifleştir (User)
@router.put("/user/me/deactivate")
async def deactivate_own_account(user: User = Depends(is_user)):
    return UserService.deactivate_own_account(user)