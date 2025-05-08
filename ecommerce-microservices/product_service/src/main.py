from fastapi import FastAPI
from controllers import product_controller, cart_controller, order_controller

app = FastAPI()

app.include_router(product_controller.router)
app.include_router(cart_controller.router)
app.include_router(order_controller.router)