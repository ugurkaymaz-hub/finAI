from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserCreate
from app.services.user_services import create_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def register_user(user: UserCreate):
    return create_user(user)