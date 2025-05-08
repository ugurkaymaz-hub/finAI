# Uygulamanın başlatıldığı ana dosya

from fastapi import FastAPI
from app.controllers import user_controller , auth_controller , authz_controller 
from app.controllers import address_contact_controller
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_controller.router)
app.include_router(auth_controller.router)
app.include_router(authz_controller.router)
app.include_router(address_contact_controller.router)
