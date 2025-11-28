from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.schemas import OrderCreate, Order
from app.models import Order as DBOrder
from app.utils import get_db

router = APIRouter(tags=['orders'])

@router.post('/orders/', response_model=Order)
def create_order(order: OrderCreate):
    db_order = DBOrder(user_id=order.user_id, order_date=order.order_date, total=order.total, status=order.status)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order