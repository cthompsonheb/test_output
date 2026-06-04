from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI"}

def test_read_item() -> None:
    response = client.get("/items/1?q=foo")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "foo"}

def test_create_item() -> None:
    payload = {"name": "widget", "price": 9.99, "tax": 0.5}
    response = client.post("/items", json=payload)
    assert response.status_code == 200
    assert response.json() == {"name": "widget", "total_price": 10.49}

def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_delete_item() -> None:
    response = client.delete("/items/42")
    assert response.status_code == 200
    assert response.json() == {"deleted": True, "item_id": 42}
