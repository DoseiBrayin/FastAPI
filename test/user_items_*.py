# FILEPATH: /Users/recodeair/Desktop/FastAPI/tests/test_user_controller.py
from fastapi.testclient import TestClient
from fastapi import FastAPI
from controller import user_controller
from models import Item

app = FastAPI()

app.post("/items/")(user_controller.create_item)

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Foo", "description": "A very nice Item", "price": 35.5})
    assert response.status_code == 200
    assert response.json() == {"name": "Fo", "description": "A very nice Item", "price": 35.5}