from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from models.cart_model import CartItemCreate, CartItemUpdate, CartItem

class CartRepositoryInterface(ABC):

    @abstractmethod
    def get_user_cart(self, db: Session, user_id: int) -> list[CartItem]:
        pass

    @abstractmethod
    def get_cart_item(self, db: Session, user_id: int, product_id: int) -> CartItem | None:
        pass

    @abstractmethod
    def add_to_cart(self, db: Session, user_id: int, item: CartItemCreate) -> CartItem:
        pass

    @abstractmethod
    def update_cart_item(self, db: Session, user_id: int, item: CartItemUpdate) -> CartItem:
        pass

    @abstractmethod
    def remove_from_cart(self, db: Session, user_id: int, product_id: int) -> None:
        pass

    @abstractmethod
    def clear_cart(self, db: Session, user_id: int) -> None:
        pass