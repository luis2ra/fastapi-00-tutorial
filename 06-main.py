# 06: Path Parameters and Numeric Validations
from typing import Optional

# Import Path
from fastapi import FastAPI, Path, Query


app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Order the parameters as you need / omitiendo el Query
@app.get("/items2/{item_id}")
async def read_items2(
    q: str, 
    item_id: int = Path(..., title="The ID of the item to get")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Order the parameters as you need, tricks (Pass * as the first parameter of the function.)
@app.get("/items3/{item_id}")
async def read_items3(
    *, 
    item_id: int = Path(..., title="The ID of the item to get"),
    q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Number validations: greater than or equal
@app.get("/items4/{item_id}")
async def read_items4(
    *, 
    item_id: int = Path(..., title="The ID of the item to get", ge=1), 
    q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Number validations: greater than and less than or equal
@app.get("/items5/{item_id}")
async def read_items5(
    *,
    item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Number validations: floats, greater than and less than
@app.get("/items6/{item_id}")
async def read_items6(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
    