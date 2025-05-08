from sqlalchemy.orm import Session
from models.order_model import Order, OrderItem

def create_order(db: Session, order: Order):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_orders_by_user(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).order_by(Order.created_at.desc()).all()