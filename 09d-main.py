# 09: Body - Nested Models
from typing import Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl


app = FastAPI()


# Special types and validation
# In the Image model we have a url field, we can declare it to be instead of a str, a Pydantic's HttpUrl
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[Image] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
