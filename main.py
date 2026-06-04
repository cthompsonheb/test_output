from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def read_root() -> dict:
    return {"message": "Welcome to FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None) -> dict:
    return {"item_id": item_id, "q": q}

@app.post("/items")
def create_item(item: Item) -> dict:
    total = item.price + (item.tax or 0)
    return {"name": item.name, "total_price": total}

@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict:
    return {"deleted": True, "item_id": item_id}
