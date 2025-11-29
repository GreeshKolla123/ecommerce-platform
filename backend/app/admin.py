from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.database import get_db
from app.models import Product, Order

admin_router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

@admin_router.get("/products")
def get_products(db = Depends(get_db)):
    products = db.query(Product).all()
    return products

@admin_router.post("/products")
def create_product(product: Product, db = Depends(get_db)):
    db.add(product)
    db.commit()
    return {"message": "Product created successfully"}

@admin_router.put("/products/{product_id}")
def update_product(product_id: int, product: Product, db = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        return JSONResponse(status_code=404, content={"message": "Product not found"})
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.category = product.category
    db.commit()
    return {"message": "Product updated successfully"}

@admin_router.delete("/products/{product_id}")
def delete_product(product_id: int, db = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        return JSONResponse(status_code=404, content={"message": "Product not found"})
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}

@admin_router.get("/orders")
def get_orders(db = Depends(get_db)):
    orders = db.query(Order).all()
    return orders
