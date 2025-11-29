from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/admin/products")
    assert response.status_code == 200

def test_create_product():
    response = client.post("/admin/products", json={"name": "Test Product", "description": "Test product description", "price": 100.0, "category": "Test category"})
    assert response.status_code == 200

def test_update_product():
    response = client.put("/admin/products/1", json={"name": "Updated Test Product", "description": "Updated test product description", "price": 200.0, "category": "Updated test category"})
    assert response.status_code == 200

def test_delete_product():
    response = client.delete("/admin/products/1")
    assert response.status_code == 200

def test_get_orders():
    response = client.get("/admin/orders")
    assert response.status_code == 200
