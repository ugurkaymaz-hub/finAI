#Library imports
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

#Local imports
from src.core.database import get_db
from src.services.order_service import order_service
from src.auth.dependencies import require_user
from src.schemas.order_schema import OrderResponse


router = APIRouter(prefix="/order", tags=["Order"])

@router.post("/", response_model=OrderResponse)
def create_order(user=Depends(require_user), db: Session = Depends(get_db)):
    order = order_service.place_order(db, user["user_id"])
    if not order:
        return {"message": "Cart is empty"}
    return order

@router.get("/", response_model=List[OrderResponse])
def get_order_history(user=Depends(require_user), db: Session = Depends(get_db)):
    return order_service.get_order_history(db, user["user_id"])