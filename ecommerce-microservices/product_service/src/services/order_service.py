#Library imports
from sqlalchemy.orm import Session

# Local imports
from repositories.interfaces.order_repository import OrderRepositoryInterface
from repositories.concrete.order_repository_impl import OrderRepository
from services.cart_service import CartService
from schemas.order_schema import OrderCreate, OrderItemCreate
from models.cart_model import CartItem
from repositories.concrete.cart_repository_impl import CartRepository


class OrderService:
    def __init__(self, repo: OrderRepositoryInterface, cart_service: CartService):
        self.repo = repo
        self.cart_service = cart_service

    def place_order(self, db: Session, user_id: int):
        cart_items: list[CartItem] = self.cart_service.get_user_cart(db, user_id)
        if not cart_items:
            return None

        # Stok ve toplam hesaplama simülasyonu
        total = sum(item.quantity * item.price for item in cart_items)

        order_items = [
            OrderItemCreate(
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price
            )
            for item in cart_items
        ]

        order_data = OrderCreate(items=order_items, total_price=total)
        order = self.repo.create_order(db, user_id, order_data)

        self.cart_service.clear_cart(db, user_id)
        return order

    def get_order_history(self, db: Session, user_id: int):
        return self.repo.get_user_orders(db, user_id)
    
order_service = OrderService(
    repo = OrderRepository(), 
    cart_service=CartService(repo=CartRepository())
)