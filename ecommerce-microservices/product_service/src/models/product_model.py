#Library imports
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from typing import Optional

#Local imports
from src.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    unit_price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    image_url = Column(String, nullable=True)

    category = relationship("Category", back_populates="products")

