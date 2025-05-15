#Library imports
from sqlalchemy.orm import Session

#Local imports
from src.models.cart_model import CartItem
from src.schemas.cart_schema import CartItemCreate, CartItemUpdate
from src.repositories.interfaces.cart_repository import CartRepositoryInterface

class CartRepository(CartRepositoryInterface):

    def get_user_cart(self, db: Session, user_id: int):
        return db.query(CartItem).filter(CartItem.user_id == user_id).all()

    def get_cart_item(self, db: Session, user_id: int, product_id: int):
        return db.query(CartItem).filter(
            CartItem.user_id == user_id,
            CartItem.product_id == product_id
        ).first()

    def add_to_cart(self, db: Session, user_id: int, item: CartItemCreate):
        cart_item = CartItem(**item.dict(), user_id=user_id)
        db.add(cart_item)
        db.commit()
        db.refresh(cart_item)
        return cart_item

    def update_cart_item(self, db: Session, user_id: int, item: CartItemUpdate):
        cart_item = db.query(CartItem).filter(
            CartItem.user_id == user_id,
            CartItem.product_id == item.product_id
        ).first()
        if cart_item:
            cart_item.quantity = item.quantity
            db.commit()
            db.refresh(cart_item)
        return cart_item

    def remove_from_cart(self, db: Session, user_id: int, product_id: int):
        item = self.get_cart_item(db, user_id, product_id)
        if item:
            db.delete(item)
            db.commit()

    def clear_cart(self, db: Session, user_id: int):
        db.query(CartItem).filter(CartItem.user_id == user_id).delete()
        db.commit()