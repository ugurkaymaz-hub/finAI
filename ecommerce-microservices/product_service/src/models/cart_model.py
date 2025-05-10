from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from core.database import Base
from pydantic import BaseModel
from typing import List, Optional

class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    product_id = Column(Integer, index=True)
    quantity = Column(Integer, nullable=False)

    cart = relationship("Cart", back_populates="items")

# Pydantic models for request/response
class CartItemBase(BaseModel):
    product_id: int
    quantity: int

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(CartItemBase):
    quantity: Optional[int] = None

class CartItemResponse(CartItemBase):
    id: int
    cart_id: int

    class Config:
        from_attributes = True

class CartBase(BaseModel):
    user_id: int

class CartCreate(CartBase):
    items: List[CartItemCreate]

class CartUpdate(BaseModel):
    items: List[CartItemUpdate]

class CartResponse(CartBase):
    id: int
    created_at: datetime
    updated_at: datetime
    items: List[CartItemResponse]

    class Config:
        from_attributes = True