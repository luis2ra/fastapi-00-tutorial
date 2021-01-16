from typing import Optional, List

from fastapi import FastAPI, Query


app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Additional validation / Add more validations
@app.get("/items2/")
async def read_items2(q: Optional[str] = Query(None, min_length=3, max_length=10)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Add regular expressions
@app.get("/items3/")
async def read_items3(
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Default values
@app.get("/items4/")
async def read_items4(q: str = Query("fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# You can use ... as the first argument (es algo de Python llamado Ellipsis)
@app.get("/items5/")
async def read_items5(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Query parameter list / multiple values
@app.get("/items6/")
async def read_items6(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items


# Query parameter list / multiple values with defaults
@app.get("/items7/")
async def read_items7(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items


# Using list
@app.get("/items8/")
async def read_items8(q: list = Query([])):
    query_items = {"q": q}
    return query_items


# Declare more metadata
@app.get("/items9/")
async def read_items9(
    q: Optional[str] = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Alias parameters
@app.get("/items10/")
async def read_items10(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
    