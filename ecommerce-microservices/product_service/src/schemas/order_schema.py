from pydantic import BaseModel
from datetime import datetime
from typing import List

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
    total_price: float

class OrderItemRead(BaseModel):
    product_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True

class OrderRead(BaseModel):
    id: int
    total_price: float
    created_at: datetime
    items: List[OrderItemRead]

    class Config:
        orm_mode = True

class OrderItemResponse(BaseModel):
    product_id: int
    quantity: int
    price_at_purchase: float  # sipariş sırasında ürünün fiyatı

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: float
    created_at: datetime
    items: List[OrderItemResponse]

    class Config:
        orm_mode = True
        