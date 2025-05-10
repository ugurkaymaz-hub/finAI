from fastapi import APIRouter, Request, Depends
import requests
from app.config import get_settings
from fastapi.responses import JSONResponse

settings = get_settings()

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int, request: Request):
    """
    Kullanıcı bilgilerini user_service üzerinden alır.
    """
    # User service URL'sine yönlendir
    user_service_url = f"{settings.USER_SERVICE_URL}/users/{user_id}"
    
    # Yönlendirilen servise GET isteği atılır
    response = requests.get(user_service_url, headers=request.headers)
    
    if response.status_code != 200:
        # Servisten hata dönerse JSONResponse ile hata mesajı döndür
        return JSONResponse(status_code=response.status_code, content=response.json())
    
    # Servisten dönen başarılı yanıtı geri döndür
    return response.json()


@router.get("/products/{product_id}")
async def get_product(product_id: int, request: Request):
    """
    Ürün bilgilerini product_service üzerinden alır.
    """
    # Product service URL'sine yönlendir
    product_service_url = f"{settings.PRODUCT_SERVICE_URL}/products/{product_id}"
    
    # Yönlendirilen servise GET isteği atılır
    response = requests.get(product_service_url, headers=request.headers)
    
    if response.status_code != 200:
        # Servisten hata dönerse JSONResponse ile hata mesajı döndür
        return JSONResponse(status_code=response.status_code, content=response.json())
    
    # Servisten dönen başarılı yanıtı geri döndür
    return response.json()