from fastapi import APIRouter, Depends, HTTPException
from app.services.authz_service import AuthzService
from app.models.user import User
from app.core.security import get_current_user

router = APIRouter()

# Kullanıcının Tüm İzinlerini Getir
@router.get("/permissions", response_model=list[str])
def get_user_permissions(user: User = Depends(get_current_user)):
    """Kullanıcının tüm izinlerini döner."""
    permissions = AuthzService.get_user_permissions(user)
    if not permissions:
        raise HTTPException(status_code=404, detail="No permissions found for this user")
    return permissions

# Kullanıcı Bu Role Sahip Mi?
@router.get("/hasRole/{role}", response_model=bool)
def has_role(role: str, user: User = Depends(get_current_user)):
    """Kullanıcının belirli bir role sahip olup olmadığını kontrol eder."""
    has_role = AuthzService.has_role(user, role)
    if not has_role:
        raise HTTPException(status_code=403, detail=f"User does not have role {role}")
    return True

# Kullanıcının Belirli Permission'ı Var Mı?
@router.get("/hasPermission/{permission}", response_model=bool)
def has_permission(permission: str, user: User = Depends(get_current_user)):
    """Kullanıcının belirli bir permission'a sahip olup olmadığını kontrol eder."""
    has_permission = AuthzService.has_permission(user, permission)
    if not has_permission:
        raise HTTPException(status_code=403, detail=f"User does not have permission {permission}")
    return True




