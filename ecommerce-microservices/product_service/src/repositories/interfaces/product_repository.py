from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from models.product_model import ProductCreate, ProductUpdate, Product

class ProductRepositoryInterface(ABC):
    
    @abstractmethod
    def get_all(self, db: Session) -> list[Product]:
        pass

    @abstractmethod
    def get_by_id(self, db: Session, product_id: int) -> Product | None:
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