from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200

def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200

    response = client.get("/products/999")
    assert response.status_code == 404
