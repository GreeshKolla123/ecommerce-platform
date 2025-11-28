from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str

    class Config:
        orm_mode = True

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int

class CartItem(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: int
    order_date: str
    total: float
    status: str

class Order(BaseModel):
    id: int
    user_id: int
    order_date: str
    total: float
    status: str

    class Config:
        orm_mode = True