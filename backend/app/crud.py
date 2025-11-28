from app.models import User, Product, Order, OrderItem
from app.database import SessionLocal

# User CRUD

def get_user(db, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db, username: str, email: str, password: str):
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Product CRUD

def get_product(db, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db, name: str, description: str, price: float):
    product = Product(name=name, description=description, price=price)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Order CRUD

def get_order(db, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def create_order(db, user_id: int, status: str, total: float):
    order = Order(user_id=user_id, status=status, total=total)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

# Order Item CRUD

def get_order_item(db, order_item_id: int):
    return db.query(OrderItem).filter(OrderItem.id == order_item_id).first()

def create_order_item(db, order_id: int, product_id: int, quantity: int):
    order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=quantity)
    db.add(order_item)
    db.commit()
    db.refresh(order_item)
    return order_item
