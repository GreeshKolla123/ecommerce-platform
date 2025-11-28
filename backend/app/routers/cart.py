from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.schemas import CartItemCreate, CartItem
from app.models import CartItem as DBCartItem
from app.utils import get_db

router = APIRouter(tags=['cart'])

@router.post('/cart/', response_model=CartItem)
def create_cart_item(cart_item: CartItemCreate):
    db_cart_item = DBCartItem(user_id=cart_item.user_id, product_id=cart_item.product_id, quantity=cart_item.quantity)
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item