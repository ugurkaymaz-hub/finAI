from fastapi import FastAPI
from app.routes.proxy_routes import router as proxy_router
from app.middlewares.auth_middleware import AuthMiddleware
from starlette.middleware import Middleware


# Middleware listesi
middleware = [
    Middleware(AuthMiddleware)
]

# FastAPI uygulaması tanımı
app = FastAPI(middleware=middleware)


# Router (API endpoint yönlendirme)
app.include_router(proxy_router)

@app.get("/")
def read_root():
    return {"message": "Gateway is running"}