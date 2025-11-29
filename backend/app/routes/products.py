from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.models import Product
from app.database import engine

products_router = APIRouter()

@products_router.get("/products")
def get_products():
    products = Product.query.all()
    return JSONResponse(content=[product.__dict__ for product in products], media_type="application/json")

@products_router.get("/products/{product_id}")
def get_product(product_id: int):
    product = Product.query.filter_by(id=product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return JSONResponse(content=product.__dict__, media_type="application/json")