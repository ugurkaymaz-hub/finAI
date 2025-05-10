from app.models.address_contact import Address_Contact
from app.models.user import User
from app.core.database import SessionLocal
from fastapi import HTTPException


class AddressRepository:

    @staticmethod
    def get_addresses_for_user(user: User):
        """Kullanıcının adreslerini veritabanından alır."""
        db = SessionLocal()
        addresses = db.query(Address_Contact).filter(Address_Contact.user_id == user.id).all()
        db.close()
        return addresses

    @staticmethod
    def add_address_for_user(user: User, address: Address_Contact):
        """Kullanıcıya yeni bir adres ekler."""
        db = SessionLocal()
        address.user_id = user.id
        db.add(address)
        db.commit()
        db.refresh(address)
        db.close()
        return address

    @staticmethod
    def update_address_for_user(user: User, address_id: int, address: Address_Contact):
        """Kullanıcı adresini günceller."""
        db = SessionLocal()
        existing_address = db.query(Address_Contact).filter(Address_Contact.id == address_id, Address_Contact.user_id == user.id).first()
        if not existing_address:
            db.close()
            return None
        existing_address.street = address.street
        existing_address.city = address.city
        existing_address.zip_code = address.zip_code
        db.commit()
        db.refresh(existing_address)
        db.close()
        return existing_address

    @staticmethod
    def delete_address_for_user(user: User, address_id: int):
        """Kullanıcının adresini siler."""
        db = SessionLocal()
        address = db.query(Address_Contact).filter(Address_Contact.id == address_id, Address_Contact.user_id == user.id).first()
        if not address:
            db.close()
            return None
        db.delete(address)
        db.commit()
        db.close()
        return address