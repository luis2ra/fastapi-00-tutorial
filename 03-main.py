# 03: Query Parameters
from typing import Optional

from fastapi import FastAPI


app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


'''
Defaults
As query parameters are not a fixed part of a path, they can be optional and can have default values.
'''
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

'''
Optional parameters
The same way, you can declare optional query parameters, by setting their default to None.
'''
@app.get("/items-v2/{item_id}")
async def read_item_v2(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

'''
Query parameter type conversion
You can also declare bool types, and they will be converted.
'''
@app.get("/items-v3/{item_id}")
async def read_item_v3(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

'''
Multiple path and query parameters
You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.

And you don't have to declare them in any specific order.
'''
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

'''
Required query parameters
When you declare a default value for non-path parameters (for now, we have only seen query parameters), then it is not required.

If you don't want to add a specific value but just make it optional, set the default as None.

But when you want to make a query parameter required, you can just not declare any default value.
'''
@app.get("/items-v4/{item_id}")
async def read_item_v4(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


'''
You can define some parameters as required, some as having a default value, and some entirely optional.
'''
@app.get("/items-v5/{item_id}")
async def read_item_v5(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item