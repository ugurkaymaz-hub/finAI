#Library imports
from sqlalchemy.orm import Session

# Local imports
from src.repositories.interfaces.cart_repository import CartRepositoryInterface
from src.repositories.concrete.cart_repository_impl import CartRepository
from src.schemas.cart_schema import CartItemCreate, CartItemUpdate

class CartService:
    def __init__(self, repo: CartRepositoryInterface):
        self.repo = repo

    def get_user_cart(self, db: Session, user_id: int):
        return self.repo.get_user_cart(db, user_id)

    def get_cart_item(self, db: Session, user_id: int, product_id: int):
        return self.repo.get_cart_item(db, user_id, product_id)

    def add_to_cart(self, db: Session, user_id: int, item: CartItemCreate):
        return self.repo.add_to_cart(db, user_id, item)

    def update_cart_item(self, db: Session, user_id: int, item: CartItemUpdate):
        return self.repo.update_cart_item(db, user_id, item)

    def remove_from_cart(self, db: Session, user_id: int, product_id: int):
        return self.repo.remove_from_cart(db, user_id, product_id)

    def clear_cart(self, db: Session, user_id: int):
        return self.repo.clear_cart(db, user_id)
    

cart_service = CartService(CartRepository())