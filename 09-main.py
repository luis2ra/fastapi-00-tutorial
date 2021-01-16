from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# List fields  (You can define an attribute to be a subtype. For example, a Python list)
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
