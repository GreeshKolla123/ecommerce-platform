from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.database import get_db
from app.models import Product

products_router = APIRouter(
    prefix="/products",
    tags=["products"],
)

@products_router.get("/")
def get_products(db = Depends(get_db)):
    products = db.query(Product).all()
    return products

@products_router.get("/{product_id}")
def get_product(product_id: int, db = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        return JSONResponse(status_code=404, content={"message": "Product not found"})
    return product
