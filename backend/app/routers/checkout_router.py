from fastapi import APIRouter, Depends
from app.models import Order
from app.schemas import OrderCreate
from app.utils.db import get_db

from app.utils.auth import get_current_user

checkout_router = APIRouter()

@checkout_router.post('/api/checkout')
def checkout(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    order_in = Order(user_id=current_user.id, total=order.total, status=order.status)
    db.add(order_in)
    db.commit()
    return {'order': order_in}
