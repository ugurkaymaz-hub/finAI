#Library imports
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

#Local imports
from src.models.order_model import Order
from src.schemas.order_schema import OrderCreate 

class OrderRepositoryInterface(ABC):

    @abstractmethod
    def create_order(self, db: Session, user_id: int, order_data: OrderCreate) -> Order:
        pass

    @abstractmethod
    def get_user_orders(self, db: Session, user_id: int) -> list[Order]:
        pass