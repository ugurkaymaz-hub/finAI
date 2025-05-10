from pydantic import BaseModel
from typing import Optional

class AddressContact(BaseModel):
    id: int
    user_id: int
    address: str
    city: str
    postal_code: str
    phone: Optional[str] = None

    class Config:
        orm_mode = True