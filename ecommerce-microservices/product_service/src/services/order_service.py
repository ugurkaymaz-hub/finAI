from sqlalchemy.orm import Session
from models.order_model import Order, OrderItem
from models.cart_model import CartItem
from repositories import order_repository, cart_repository

def create_order_from_cart(db: Session, user_id: int):
    cart_items = cart_repository.get_cart_items_by_user(db, user_id)
    if not cart_items:
        return None

    order = Order(user_id=user_id)
    db.add(order)
    db.flush()  # Order ID'yi alabilmek için

    order_items = []
    for item in cart_items:
        order_items.append(OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=0.0  # opsiyonel: fiyat bilgisi product tablosundan alınabilir
        ))

    db.add_all(order_items)
    cart_repository.clear_cart(db, user_id)  # sepeti temizle
    db.commit()
    db.refresh(order)
    return order

def get_user_orders(db: Session, user_id: int):
    return order_repository.get_orders_by_user(db, user_id)