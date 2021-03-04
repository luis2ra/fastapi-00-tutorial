# 09: Body - Nested Models
from typing import List, Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl


app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


# Attributes with lists of submodels
# You can also use Pydantic models as subtypes of list, set, etc.
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results