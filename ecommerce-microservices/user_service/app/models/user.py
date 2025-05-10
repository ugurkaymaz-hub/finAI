 # Kullanıcı modeli burada tanımlanır

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy import Boolean
from app.models.address_contact import Address_Contact

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)  # 1: active, 0: inactive
    role = Column(String, default="user")  # "admin" veya "user"
    addresses = relationship("Address_Contact", back_populates="user")




    