from sqlalchemy.orm import Session
from models.order_model import Order, OrderItem, OrderCreate
from repositories.interfaces.order_repository import OrderRepositoryInterface

class OrderRepository(OrderRepositoryInterface):

    def create_order(self, db: Session, user_id: int, order_data: OrderCreate):
        order = Order(user_id=user_id, total_price=order_data.total_price)
        db.add(order)
        db.flush()  # order.id üretildi

        for item in order_data.items:
            db_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price
            )
            db.add(db_item)

        db.commit()
        db.refresh(order)
        return order

    def get_user_orders(self, db: Session, user_id: int):
        return db.query(Order).filter(Order.user_id == user_id).all()