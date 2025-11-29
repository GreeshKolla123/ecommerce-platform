from fastapi import APIRouter, Depends
from app.models import Order
from app.schemas import OrderCreate
from app.utils.db import get_db

from app.utils.auth import get_current_user

orders_router = APIRouter()

@orders_router.get('/api/orders')
def get_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    orders = db.query(Order).filter(Order.user_id == current_user.id).all()
    return {'orders': orders}

@orders_router.get('/api/orders/{order_id}')
def get_order(order_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    order = db.query(Order).filter(Order.id == order_id).first()
    return {'order': order}
