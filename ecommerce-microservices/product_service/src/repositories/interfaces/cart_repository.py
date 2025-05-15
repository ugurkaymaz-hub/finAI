#Library imports
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from typing import Optional

#Local imports
from src.models.cart_model import CartItem
from src.schemas.cart_schema import CartItemCreate, CartItemUpdate

class CartRepositoryInterface(ABC):

    @abstractmethod
    def get_user_cart(self, db: Session, user_id: int) -> list[CartItem]:
        pass

    @abstractmethod
    def get_cart_item(self, db: Session, user_id: int, product_id: int) -> Optional[CartItem]:
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