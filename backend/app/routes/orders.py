from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.models import Order
from app.database import engine

orders_router = APIRouter()

@orders_router.post("/orders")
def place_order(order: Order):
    db.session.add(order)
    db.session.commit()
    return JSONResponse(content={"message": "Order placed successfully"}, media_type="application/json")

@orders_router.get("/orders")
def get_orders():
    orders = Order.query.all()
    return JSONResponse(content=[order.__dict__ for order in orders], media_type="application/json")

@orders_router.get("/orders/{order_id}")
def get_order(order_id: int):
    order = Order.query.filter_by(id=order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return JSONResponse(content=order.__dict__, media_type="application/json")