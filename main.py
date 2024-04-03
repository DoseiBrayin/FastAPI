# main.py
from fastapi import FastAPI
from models import user_model
from controller import user_controller

app = FastAPI()
# Aquí estamos definiendo las rutas de nuestra API
@app.get("/items/{item_id}", response_model=user_model.Item)
def read_item(item_id: int):
    return user_controller.get_item(item_id)

@app.get("/items/", response_model=list[user_model.Item])
def read_items():
    return user_controller.get_items()

@app.post("/items/", response_model=user_model.Item)
def create_item(item: user_model.Item):
    return user_controller.create_item(item)

