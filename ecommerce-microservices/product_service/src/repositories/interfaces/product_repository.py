#Library imports
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from typing import Optional

#Local imports
from src.schemas.product_schema import ProductCreate, ProductUpdate
from src.models.product_model import Product

class ProductRepositoryInterface(ABC):
    
    @abstractmethod
    def get_all(self, db: Session) -> list[Product]:
        pass

    @abstractmethod
    def get_by_id(self, db: Session, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def create(self, db: Session, product: ProductCreate) -> Product:
        pass

    @abstractmethod
    def update(self, db: Session, product_id: int, product: ProductUpdate) -> Product:
        pass

    @abstractmethod
    def delete(self, db: Session, product_id: int) -> None:
        pass