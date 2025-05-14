from pydantic import BaseModel
from typing import Literal ,  Optional


class UserCreate(BaseModel):
    username: str
    password: str
    e_mail: str
    full_name: str
    is_active: bool = True
    role: Literal["user", "admin"] = "user"


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[Literal["user", "admin"]] = None

class UserPasswordChangeRequest(BaseModel):
    old_password: str
    new_password: str