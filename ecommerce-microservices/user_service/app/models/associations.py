from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database import Base

role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("roles.id")),
    Column("permission_id", Integer, ForeignKey("permissions.id")),
)

user_permissions = Table(
    "user_permissions",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("permission_id", Integer, ForeignKey("permissions.id")),
)