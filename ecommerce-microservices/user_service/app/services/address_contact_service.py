from app.repositories.address_contact_repository import AddressRepository
from app.models.user import User
from app.models.address_contact import Address
from fastapi import HTTPException


class AddressService:

    @staticmethod
    def get_addresses_for_user(user: User):
        """Kullanıcının tüm adreslerini döner."""
        return AddressRepository.get_addresses_for_user(user)

    @staticmethod
    def add_address_for_user(user: User, address: Address):
        """Kullanıcının yeni bir adres eklemesini sağlar."""
        return AddressRepository.add_address_for_user(user, address)

    @staticmethod
    def update_address_for_user(user: User, address_id: int, address: Address):
        """Kullanıcının adresini günceller."""
        return AddressRepository.update_address_for_user(user, address_id, address)

    @staticmethod
    def delete_address_for_user(user: User, address_id: int):
        """Kullanıcının adresini siler."""
        return AddressRepository.delete_address_for_user(user, address_id)