# models.py
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float