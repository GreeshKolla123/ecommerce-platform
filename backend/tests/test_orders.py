from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_place_order():
    response = client.post("/orders", json={"user_id": 1, "date": "2022-01-01", "total": 100.0})
    assert response.status_code == 200

def test_get_orders():
    response = client.get("/orders")
    assert response.status_code == 200
