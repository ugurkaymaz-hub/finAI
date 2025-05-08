from sqlalchemy.orm import Session
from repositories.interfaces.product_repository import ProductRepositoryInterface
from models.product_model import ProductCreate, ProductUpdate

class ProductService:
    def __init__(self, repo: ProductRepositoryInterface):
        self.repo = repo

    def get_all_products(self, db: Session):
        return self.repo.get_all(db)

    def get_product_by_id(self, db: Session, product_id: int):
        return self.repo.get_by_id(db, product_id)

    def create_product(self, db: Session, product_data: ProductCreate):
        return self.repo.create(db, product_data)

    def update_product(self, db: Session, product_id: int, product_data: ProductUpdate):
        return self.repo.update(db, product_id, product_data)

    def delete_product(self, db: Session, product_id: int):
        return self.repo.delete(db, product_id)

