# Uygulamanın başlatıldığı ana dosya

from fastapi import FastAPI
from app.controllers import user_controller
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_controller.router)