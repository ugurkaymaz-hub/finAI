from fastapi import APIRouter, Depends, HTTPException
from app.services.address_contact_service import AddressService
from app.models.user import User
from app.schemas.address_contact_schema import AddressContact
from app.core.auth import get_current_user


router = APIRouter(prefix="/address", tags=["Address"] )

# Adresleri Listele
@router.get("/", response_model=list[AddressContact])
def list_addresses(user: User = Depends(get_current_user)):
    """Kullanıcının tüm adreslerini döner."""
    addresses = AddressService.get_addresses_for_user(user)
    if not addresses:
        raise HTTPException(status_code=404, detail="No addresses found for this user")
    return addresses

# Yeni Adres Ekle
@router.post("/", response_model=AddressContact)
def add_address(address: AddressContact, user: User = Depends(get_current_user)):
    """Yeni bir adres ekler."""
    new_address = AddressService.add_address_for_user(user, address)
    if not new_address:
        raise HTTPException(status_code=400, detail="Failed to add address")
    return new_address

# Adres Güncelle
@router.put("/{address_id}", response_model=AddressContact)
def update_address(address_id: int, address: AddressContact, user: User = Depends(get_current_user)):
    """Verilen ID'ye sahip adresi günceller."""
    updated_address = AddressService.update_address_for_user(user, address_id, address)
    if not updated_address:
        raise HTTPException(status_code=404, detail="Address not found or failed to update")
    return updated_address

# Adres Sil
@router.delete("/{address_id}", response_model=AddressContact)
def delete_address(address_id: int, user: User = Depends(get_current_user)):
    """Verilen ID'ye sahip adresi siler."""
    deleted_address = AddressService.delete_address_for_user(user, address_id)
    if not deleted_address:
        raise HTTPException(status_code=404, detail="Address not found or failed to delete")
    return deleted_address