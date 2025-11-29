from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.models import Cart
from app.database import engine

 cart_router = APIRouter()

@cart_router.post("/cart")
def add_to_cart(cart: Cart):
    db.session.add(cart)
    db.session.commit()
    return JSONResponse(content={"message": "Product added to cart successfully"}, media_type="application/json")

@cart_router.get("/cart")
def get_cart():
    cart = Cart.query.all()
    return JSONResponse(content=[item.__dict__ for item in cart], media_type="application/json")