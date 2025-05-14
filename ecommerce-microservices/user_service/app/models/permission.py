from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.associations import role_permissions, user_permissions
from app.models.role import Role
from app.models.user import User


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    users = relationship("User", secondary=user_permissions , back_populates="permissions")
    roles = relationship("Role", secondary=role_permissions , back_populates="permissions")
