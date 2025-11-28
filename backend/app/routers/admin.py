from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.schemas import User, Product, CartItem, Order
from app.models import User as DBUser, Product as DBProduct, CartItem as DBCartItem, Order as DBOrder
from app.utils import get_db

router = APIRouter(tags=['admin'])

@router.get('/admin/users/', response_model=list[User])
def read_users():
    users = get_db().query(DBUser).all()
    return users

@router.get('/admin/products/', response_model=list[Product])
def read_products():
    products = get_db().query(DBProduct).all()
    return products

@router.get('/admin/cart/', response_model=list[CartItem])
def read_cart():
    cart_items = get_db().query(DBCartItem).all()
    return cart_items

@router.get('/admin/orders/', response_model=list[Order])
def read_orders():
    orders = get_db().query(DBOrder).all()
    return orders