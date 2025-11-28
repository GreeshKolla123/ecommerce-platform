from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.schemas import ProductCreate, Product
from app.models import Product as DBProduct
from app.utils import get_db

router = APIRouter(tags=['products'])

@router.get('/products/', response_model=list[Product])
def read_products():
    products = get_db().query(DBProduct).all()
    return products

@router.get('/products/{product_id}', response_model=Product)
def read_product(product_id: int):
    product = get_db().query(DBProduct).filter(DBProduct.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product