from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.cart_schema import CartItemCreate, CartItemUpdate
from services import cart_service
from auth.dependencies import require_user  # Kullanıcıyı JWT'den ayıklayan yardımcı fonksiyon

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/")
def get_cart(user=Depends(require_user), db: Session = Depends(get_db)):
    return cart_service.get_user_cart(db, user["user_id"])

@router.get("/{product_id}")
def get_item_detail(product_id: int, user=Depends(require_user), db: Session = Depends(get_db)):
    return cart_service.get_cart_item_detail(db, user["user_id"], product_id)

@router.post("/")
def add_item_to_cart(data: CartItemCreate, user=Depends(require_user), db: Session = Depends(get_db)):
    return cart_service.add_to_cart(db, user["user_id"], data)

@router.put("/{product_id}")
def update_item_quantity(product_id: int, data: CartItemUpdate, user=Depends(require_user), db: Session = Depends(get_db)):
    return cart_service.update_cart_item_quantity(db, user["user_id"], product_id, data.quantity)

@router.delete("/{product_id}")
def remove_item(product_id: int, user=Depends(require_user), db: Session = Depends(get_db)):
    return cart_service.remove_from_cart(db, user["user_id"], product_id)

@router.delete("/")
def clear_user_cart(user=Depends(require_user), db: Session = Depends(get_db)):
    return cart_service.clear_cart(db, user["user_id"])