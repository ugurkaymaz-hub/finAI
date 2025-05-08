from fastapi import APIRouter, Depends, HTTPException
from auth.dependencies import get_current_user, require_admin

router = APIRouter(prefix="/product", tags=["Product"])

@router.get("/")
def list_products(user=Depends(get_current_user)):
    # Tüm ürünleri listele
    return {"message": "Tüm ürünler listelendi."}

@router.get("/{product_id}")
def get_product_detail(product_id: int, user=Depends(get_current_user)):
    # Ürün detay
    return {"message": f"Ürün detay: {product_id}"}

@router.post("/")
def create_product(data: dict, user=Depends(require_admin)):
    # Yeni ürün ekle
    return {"message": "Yeni ürün eklendi."}

@router.post("/bulk")
def create_bulk_products(data: list[dict], user=Depends(require_admin)):
    # Toplu ürün ekle
    return {"message": "Toplu ürünler eklendi."}

@router.put("/{product_id}")
def update_product(product_id: int, data: dict, user=Depends(require_admin)):
    # Ürün güncelle
    return {"message": f"Ürün güncellendi: {product_id}"}

@router.delete("/{product_id}")
def delete_product(product_id: int, user=Depends(require_admin)):
    # Ürün sil
    return {"message": f"Ürün silindi: {product_id}"}