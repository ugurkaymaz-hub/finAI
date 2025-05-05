from app.models.user import User
from app.core.database import SessionLocal
from app.models.role import Role  # Role modeline bağlı olarak değişebilir
from app.models.permission import Permission  # Permission modeline bağlı olarak değişebilir


class AuthzRepository:

    @staticmethod
    def get_roles_for_user(user: User):
        """Kullanıcının rollerini veritabanından alır."""
        db = SessionLocal()
        roles = db.query(Role).filter(Role.users.any(id=user.id)).all()
        db.close()
        return [role.name for role in roles]

    @staticmethod
    def get_permissions_for_user(user: User):
        """Kullanıcının izinlerini veritabanından alır."""
        db = SessionLocal()
        permissions = db.query(Permission).filter(Permission.users.any(id=user.id)).all()
        db.close()
        return [permission.name for permission in permissions]