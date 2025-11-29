from fastapi import APIRouter, Depends
from app.models import Product
from app.schemas import ProductCreate
from app.utils.db import get_db

products_router = APIRouter()

@products_router.get('/api/products')
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return {'products': products}

@products_router.get('/api/products/{product_id}')
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    return {'product': product}
