from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class LogoutResponse(BaseModel):
    msg: str = "User logged out successfully"
    class Config:
        from_attributes = True