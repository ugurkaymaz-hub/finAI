from app.repositories.authz_repository import AuthzRepository
from app.models.user import User
from fastapi import HTTPException


class AuthzService:

    @staticmethod
    def get_user_permissions(user: User):
        """Kullanıcının tüm izinlerini döner."""
        permissions = AuthzRepository.get_permissions_for_user(user)
        return permissions

    @staticmethod
    def has_role(user: User, role: str) -> bool:
        """Kullanıcının belirli bir role sahip olup olmadığını kontrol eder."""
        roles = AuthzRepository.get_roles_for_user(user)
        return role in roles

    @staticmethod
    def has_permission(user: User, permission: str) -> bool:
        """Kullanıcının belirli bir permission'a sahip olup olmadığını kontrol eder."""
        permissions = AuthzRepository.get_permissions_for_user(user)
        return permission in permissions