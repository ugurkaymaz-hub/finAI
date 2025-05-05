from app.schemas.user_schema import UserCreate
from app.repositories.user_repository import save_user
from app.core.security import hash_password

def create_user(user: UserCreate):
    user.password = hash_password(user.password)
    return save_user(user)