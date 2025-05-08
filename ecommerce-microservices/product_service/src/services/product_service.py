from sqlalchemy.orm import Session
from models.product_model import Product
from schemas.product_schema import ProductCreate, ProductUpdate
from repositories import product_repository

def get_all_products(db: Session):
    return product_repository.get_all_products(db)

def get_product_by_id(db: Session, product_id: int):
    return product_repository.get_product_by_id(db, product_id)

def create_product(db: Session, product_data: ProductCreate):
    product = Product(**product_data.dict())
    return product_repository.create_product(db, product)

def create_bulk_products(db: Session, products_data: list[ProductCreate]):
    products = [Product(**item.dict()) for item in products_data]
    return product_repository.create_bulk_products(db, products)

def update_product(db: Session, product_id: int, updates: ProductUpdate):
    product = product_repository.get_product_by_id(db, product_id)
    if not product:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(product, key, value)
    return product_repository.update_product(db, product)

def delete_product(db: Session, product_id: int):
    product = product_repository.get_product_by_id(db, product_id)
    if not product:
        return None
    return product_repository.delete_product(db, product)