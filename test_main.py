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
