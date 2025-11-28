# ecommerce-platform

A comprehensive e-commerce platform with user authentication, product catalog, shopping cart, order management, and admin panel.

## Tech Stack

- **Frontend**: React + Vite
- **Backend**: FastAPI + SQLAlchemy
- **Design**: Figma ([View Design](https://www.figma.com/design/PZRTnjD8w7dfHn9fm4J9KE/Untitled?m=auto&t=GPC3ETfnqjs2ajai-6))

## Project Structure

```
ecommerce-platform/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- user authentication
- product catalog
- shopping cart
- order management
- admin panel

## API Endpoints

- `POST /api/register` - Register a new user
- `POST /api/login` - Login an existing user
- `GET /api/products` - Get a list of all products
- `GET /api/products/{id}` - Get a single product by ID
- `POST /api/cart` - Add a product to the cart
- `GET /api/cart` - Get the cart contents
- `POST /api/checkout` - Checkout and make a payment
- `GET /api/orders` - Get a list of all orders
- `GET /api/orders/{id}` - Get a single order by ID
- `PUT /api/orders/{id}` - Update an order

## License

MIT
