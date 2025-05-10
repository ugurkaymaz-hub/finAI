# schemas/address_contact.py

from pydantic import BaseModel, Field
from typing import Literal, Optional


class AddressContactBase(BaseModel):
    # Hem adres hem de iletişim tipleri için ortak özellikler
    address_type: Literal["home", "work"] = Field(..., description="Adresin/İletişimin tipi: ev veya iş")
    phone: Optional[str] = None  # İletişim bilgisi
    email: Optional[str] = None  # İletişim bilgisi
    street: Optional[str] = None  # Adres bilgisi
    city: Optional[str] = None  # Adres bilgisi
    state: Optional[str] = None  # Adres bilgisi
    postal_code: Optional[str] = None  # Adres bilgisi
    country: Optional[str] = "Türkiye"  # Varsayılan olarak Türkiye


class AddressContactCreate(AddressContactBase):
    user_id: int  # Kullanıcıya bağlanmak için (isteğe bağlı)


class AddressContactUpdate(BaseModel):
    phone: Optional[str] = None
    email: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    address_type: Optional[Literal["home", "work"]] = None


class AddressContactResponse(AddressContactBase):
    id: int

    class Config:
        orm_mode = True