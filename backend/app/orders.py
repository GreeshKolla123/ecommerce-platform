from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.database import get_db
from app.models import Order

orders_router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)

@orders_router.post("/")
def place_order(order: Order, db = Depends(get_db)):
    db.add(order)
    db.commit()
    return {"message": "Order placed successfully"}

@orders_router.get("/")
def get_orders(db = Depends(get_db)):
    orders = db.query(Order).all()
    return orders
