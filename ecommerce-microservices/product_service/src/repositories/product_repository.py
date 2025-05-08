from sqlalchemy.orm import Session
from models.product_model import Product

def get_all_products(db: Session):
    return db.query(Product).filter(Product.is_active == True).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id, Product.is_active == True).first()

def create_product(db: Session, product: Product):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def create_bulk_products(db: Session, products: list[Product]):
    db.add_all(products)
    db.commit()
    return products

def update_product(db: Session, product: Product):
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product: Product):
    db.delete(product)
    db.commit()
    return True