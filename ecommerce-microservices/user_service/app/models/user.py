# models/user.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.associations import user_permissions


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)  # 1: active, 0: inactive
    e_mail = Column(String, unique=True, index=True)
    phone = Column(String(20) , unique=True)

    
    # Adresler ile ilişki tanımlaması
    addresses = relationship("Address_Contact" , back_populates="user")

    # Role ile ilişki tanımlaması
    role_id = Column(Integer, ForeignKey("roles.id"))  # Role'ye bağlayan foreign key
    role  = relationship("Role", back_populates="users")

    permissions = relationship("Permission" , secondary=user_permissions , back_populates="users")

    


    