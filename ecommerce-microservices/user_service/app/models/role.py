# models/role.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.permission import Permission

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Kullanıcılarla ilişki tanımlaması
    users = relationship("User", back_populates="role")
    permissions = relationship("Permission", secondary="role_permissions")