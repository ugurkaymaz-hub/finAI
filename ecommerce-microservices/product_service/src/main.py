from fastapi import FastAPI
from src.controllers import product_controller, cart_controller, order_controller
from src.core.database import engine, Base
from src.models import product_model, cart_model, order_model, category_model

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(product_controller.router)
app.include_router(cart_controller.router)
app.include_router(order_controller.router)





