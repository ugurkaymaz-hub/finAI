from sqlalchemy.orm import Session
from models.cart_model import CartItem
from schemas.cart_schema import CartItemCreate, CartItemUpdate
from repositories import cart_repository

def get_user_cart(db: Session, user_id: int):
    return cart_repository.get_cart_items_by_user(db, user_id)

def get_cart_item_detail(db: Session, user_id: int, product_id: int):
    return cart_repository.get_cart_item(db, user_id, product_id)

def add_to_cart(db: Session, user_id: int, data: CartItemCreate):
    existing = cart_repository.get_cart_item(db, user_id, data.product_id)
    if existing:
        existing.quantity += data.quantity
        return cart_repository.update_cart_item(db, existing)
    new_item = CartItem(user_id=user_id, **data.dict())
    return cart_repository.create_cart_item(db, new_item)

def update_cart_item_quantity(db: Session, user_id: int, product_id: int, quantity: int):
    item = cart_repository.get_cart_item(db, user_id, product_id)
    if item:
        item.quantity = quantity
        return cart_repository.update_cart_item(db, item)
    return None

def remove_from_cart(db: Session, user_id: int, product_id: int):
    item = cart_repository.get_cart_item(db, user_id, product_id)
    if item:
        return cart_repository.delete_cart_item(db, item)
    return False

def clear_cart(db: Session, user_id: int):
    return cart_repository.clear_cart(db, user_id)