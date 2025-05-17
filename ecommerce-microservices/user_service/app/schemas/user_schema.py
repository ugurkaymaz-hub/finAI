from pydantic import BaseModel
from typing import Literal ,  Optional

class UserBase(BaseModel):
    username: str
    e_mail: str
    full_name: str
    is_active: bool = True
    role: Literal["user", "admin"] = "user"
    phone : str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str
    e_mail: str
    full_name: str
    is_active: bool = True
    role: Literal["user", "admin"] = "user"
    phone : str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[Literal["user", "admin"]] = None

class UserPasswordChangeRequest(BaseModel):
    old_password: str
    new_password: str

#Resonse Models 

class UserResponse(BaseModel):
    id: int
    username: str
    full_name: str
    e_mail: str
    phone: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True

class UserDeleteResponse(BaseModel):
    message: str =  "User deleted successfully"  

    class Config:
        from_attributes = True

class UserCreateResponse(BaseModel):
    message: str =  "User created successfully"  
    created_user: UserResponse

    class Config:
        from_attributes = True

class UserDeactivateResponse(BaseModel):
    message: str =  "User deactivated successfully"  
    deactivated_user: UserResponse

    class Config:
        from_attributes = True

class UserChangePasswordResponse(BaseModel):
    message: str =  "Password changed successfully"  
    user: UserResponse

    class Config:
        from_attributes = True