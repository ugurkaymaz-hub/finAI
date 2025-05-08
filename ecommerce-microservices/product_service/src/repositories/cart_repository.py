from sqlalchemy.orm import Session
from models.cart_model import CartItem

def get_cart_items_by_user(db: Session, user_id: int):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()

def get_cart_item(db: Session, user_id: int, product_id: int):
    return db.query(CartItem).filter(CartItem.user_id == user_id, CartItem.product_id == product_id).first()

def create_cart_item(db: Session, cart_item: CartItem):
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

def update_cart_item(db: Session, cart_item: CartItem):
    db.commit()
    db.refresh(cart_item)
    return cart_item

def delete_cart_item(db: Session, cart_item: CartItem):
    db.delete(cart_item)
    db.commit()
    return True

def clear_cart(db: Session, user_id: int):
    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    db.commit()