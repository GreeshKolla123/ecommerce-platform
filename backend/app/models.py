from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    orders = relationship('Order', backref='user')

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    cart_items = relationship('CartItem', backref='product')

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, category='{self.category}')"

class CartItem(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    user = relationship('User', backref='cart_items')
    product = relationship('Product', backref='cart_items')

    def __repr__(self):
        return f"CartItem(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity})"

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    total = Column(Float, nullable=False)
    status = Column(String, nullable=False)

    def __repr__(self):
        return f"Order(id={self.id}, user_id={self.user_id}, order_date='{self.order_date}', total={self.total}, status='{self.status}')"