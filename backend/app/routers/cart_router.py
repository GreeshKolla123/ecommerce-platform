from fastapi import APIRouter, Depends
from app.models import CartItem
from app.schemas import CartItemCreate
from app.utils.db import get_db

from app.utils.auth import get_current_user

cart_router = APIRouter()

@cart_router.post('/api/cart')
def add_to_cart(cart_item: CartItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cart_item_in = CartItem(product_id=cart_item.product_id, user_id=current_user.id, quantity=cart_item.quantity)
    db.add(cart_item_in)
    db.commit()
    return {'cart': cart_item_in}

@cart_router.get('/api/cart')
def get_cart(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cart_items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()
    return {'cart': cart_items}
