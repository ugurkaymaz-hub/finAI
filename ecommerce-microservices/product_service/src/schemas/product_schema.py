#Library imports
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime

#Local imports
from schemas.category_schema import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    category_id: int
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    is_active: bool = True
    sku: str = Field(..., min_length=3, max_length=20)
    image_url: Optional[str] = None

    @validator('price')
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than 0')
        return round(v, 2)

    @validator('stock')
    def validate_stock(cls, v):
        if v < 0:
            raise ValueError('Stock cannot be negative')
        return v

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    category_id: Optional[int]
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    is_active: Optional[bool]
    sku: Optional[str] = Field(None, min_length=3, max_length=20)
    image_url: Optional[str]

    @validator('price')
    def validate_price(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Price must be greater than 0')
        return round(v, 2) if v is not None else v

    @validator('stock')
    def validate_stock(cls, v):
        if v is not None and v < 0:
            raise ValueError('Stock cannot be negative')
        return v

class PublicProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: CategoryResponse

    class Config:
        orm_mode = True

class AdminProductResponse(PublicProductResponse):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ProductListResponse(BaseModel):
    items: List[PublicProductResponse]
    total: int
    page: int
    size: int
    pages: int

    class Config:
        orm_mode = True

