from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    product_id = Column(Integer, index=True)
    quantity = Column(Integer, nullable=False)

    # İlişkiler (opsiyonel)
    # product = relationship("Product", back_populates="cart_items")

class CartItemCreate(Base): 
    __tablename__ = "cart_item_create"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

class CartItemUpdate(Base):
    __tablename__ = "cart_item_update"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)