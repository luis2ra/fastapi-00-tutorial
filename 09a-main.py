# import List from standard Python's typing module
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# Declare a List with a type parameter
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
