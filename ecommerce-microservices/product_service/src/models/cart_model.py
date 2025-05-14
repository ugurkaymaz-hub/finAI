#Library imports
from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import List, Optional

#Local imports
from src.core.database import Base


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
    user_id = Column(Integer, ForeignKey("carts.user_id"), index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    product_id = Column(Integer, index=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)  # ürünün sepetteki fiyatı

    cart = relationship("Cart", back_populates="items")





