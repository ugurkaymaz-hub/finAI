from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.controllers import user_controller, auth_controller, authz_controller
from app.controllers import address_contact_controller
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Swagger UI özelleştirme
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="User Service API",
        version="1.0.0",
        description="JWT token ile korunan endpoint'ler için Bearer Token kullanın.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Router'lar
app.include_router(user_controller.router)
app.include_router(auth_controller.router)
app.include_router(authz_controller.router)
app.include_router(address_contact_controller.router)