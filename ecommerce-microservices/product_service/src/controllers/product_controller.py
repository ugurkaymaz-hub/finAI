#Library imports
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

#Local imports
from auth.dependencies import get_current_user, require_admin
from schemas.product_schema import ProductCreate, ProductUpdate, PublicProductResponse , AdminProductResponse
from services.product_service import ProductService
from core.database import get_db
from repositories.concrete.product_repository_impl import ProductRepository

router = APIRouter(prefix="/products", tags=["Product"])
product_service = ProductService(repo=ProductRepository())

# Tüm ürünleri listele (herkese açık)
@router.get("/", response_model=List[PublicProductResponse])
def list_all_products(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    return product_service.get_all_products(db)


#  Ürün detay (herkese açık)
@router.get("/{product_id}", response_model=PublicProductResponse)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = product_service.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


#  Yeni ürün oluştur (sadece admin)
@router.post("/", response_model=AdminProductResponse)
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(require_admin)
):
    return product_service.create_product(db, data)


#  Toplu ürün ekle (admin)
@router.post("/bulk", response_model=List[PublicProductResponse])
def create_bulk_products(
    data: List[ProductCreate],
    db: Session = Depends(get_db),
    user: dict = Depends(require_admin)
):
    return product_service.create_bulk_products(db, data)

# Ürün güncelle (admin)
@router.put("/{product_id}", response_model=PublicProductResponse)
def update_product(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db),
    user: dict = Depends(require_admin)
):
    return product_service.update_product(db, product_id, data)

# Ürün sil (admin)
@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(require_admin)
):
    return product_service.delete_product(db, product_id)