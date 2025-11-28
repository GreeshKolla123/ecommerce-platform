from app.database import SessionLocal
from app.crud import get_user, create_user, get_product, create_product, get_order, create_order, get_order_item, create_order_item

# User CRUD

def test_get_user():
    db = SessionLocal()
    user = get_user(db, username='test_user')
    assert user is not None

# Product CRUD

def test_get_product():
    db = SessionLocal()
    product = get_product(db, product_id=1)
    assert product is not None

# Order CRUD

def test_get_order():
    db = SessionLocal()
    order = get_order(db, order_id=1)
    assert order is not None

# Order Item CRUD

def test_get_order_item():
    db = SessionLocal()
    order_item = get_order_item(db, order_item_id=1)
    assert order_item is not None
