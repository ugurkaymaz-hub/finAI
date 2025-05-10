from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models.cart_model import CartItemCreate, CartItemUpdate, CartItem
from services.cart_service import CartService
from repositories.concrete.cart_repository_impl import CartRepository
from core.database import get_db
from auth.dependencies import require_user

router = APIRouter(prefix="/cart", tags=["Cart"])

# Service ve repository instance'ları
repo = CartRepository()
cart_service = CartService(repo)

# Sepeti getir
@router.get("/", response_model=List[CartItem])
def get_cart(db: Session = Depends(get_db), user_data=Depends(require_user)):
    return cart_service.get_user_cart(db, user_id=user_data["user_id"])

# Sepetteki bir ürünün detayını getir
@router.get("/{product_id}", response_model=CartItem)
def get_cart_item(product_id: int, db: Session = Depends(get_db), user_data=Depends(require_user)):
    item = cart_service.get_cart_item(db, user_id=user_data["user_id"], product_id=product_id)
    if not item:
        raise HTTPException(status_code=404, detail="Ürün sepette bulunamadı")
    return item

# Sepete ürün ekle
@router.post("/", response_model=CartItem, status_code=status.HTTP_201_CREATED)
def add_to_cart(item: CartItemCreate, db: Session = Depends(get_db), user_data=Depends(require_user)):
    return cart_service.add_to_cart(db, user_id=user_data["user_id"], item=item)

# Sepetteki ürün adedini güncelle
@router.put("/", response_model=CartItem)
def update_cart_item(item: CartItemUpdate, db: Session = Depends(get_db), user_data=Depends(require_user)):
    updated = cart_service.update_cart_item(db, user_id=user_data["user_id"], item=item)
    if not updated:
        raise HTTPException(status_code=404, detail="Ürün sepette bulunamadı")
    return updated

# Sepetten ürün çıkar
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_from_cart(product_id: int, db: Session = Depends(get_db), user_data=Depends(require_user)):
    cart_service.remove_from_cart(db, user_id=user_data["user_id"], product_id=product_id)

# Sepeti temizle
@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def clear_cart(db: Session = Depends(get_db), user_data=Depends(require_user)):
    cart_service.clear_cart(db, user_id=user_data["user_id"])