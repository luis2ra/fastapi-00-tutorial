from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


# Request Body (Se define un modelo que recibe dicha información)
@app.post("/items/")
async def create_item(item: Item):
    return item


# Inside of the function, you can access all the attributes of the model object directly:
@app.post("/items2/")
async def create_item2(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Request body + path + query parameters
@app.post("/items3/{item_id}")
async def create_item3(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result