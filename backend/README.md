# E-commerce Platform

This is a comprehensive e-commerce platform with user authentication, product catalog, shopping cart, order management, and admin panel.

## Requirements

* FastAPI
* SQLAlchemy
* React
* Vite

## Setup

1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Create a new file named `.env` and add your secret key and algorithm
4. Run the application using `uvicorn main:app --reload`
5. Open your browser and navigate to `http://localhost:8000`

## API Endpoints

### Auth

* `POST /login`: Login to the platform
* `POST /register`: Register a new user

### Products

* `GET /products/`: Get a list of all products
* `GET /products/{product_id}`: Get a single product by ID

### Cart

* `POST /cart/`: Add a product to the cart
* `GET /cart/`: Get the cart contents

### Orders

* `POST /orders/`: Create a new order
* `GET /orders/`: Get a list of all orders

### Admin

* `GET /admin/users/`: Get a list of all users
* `GET /admin/products/`: Get a list of all products
* `GET /admin/cart/`: Get the cart contents
* `GET /admin/orders/`: Get a list of all orders