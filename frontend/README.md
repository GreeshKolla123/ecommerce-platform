# E-commerce Platform

This is a comprehensive e-commerce platform with user authentication, product catalog, shopping cart, order management, and admin panel.

## Features

* User authentication
* Product catalog
* Shopping cart
* Order management
* Admin panel

## Technical Requirements

* FastAPI
* SQLAlchemy
* React
* Vite

## Setup

1. Clone the repository
2. Install dependencies using `npm install` or `yarn install`
3. Start the development server using `npm run dev` or `yarn dev`
4. Open the application in your web browser at `http://localhost:3000`

## API Endpoints

* `GET /products`: Get a list of all products
* `GET /products/{id}`: Get a single product by ID
* `POST /cart`: Add a product to the cart
* `GET /cart`: Get the cart contents
* `POST /orders`: Create a new order
* `GET /orders`: Get a list of all orders
* `GET /orders/{id}`: Get a single order by ID
* `PUT /orders/{id}`: Update an order