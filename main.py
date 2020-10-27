from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World..."}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items2/{item_id}")
async def read_item2(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


'''
Summary:

Path Parameters

* You can declare path "parameters" or "variables" with the same syntax used by Python format strings.
* You can declare the type of a path parameter in the function, using standard Python type annotations.
* Data conversion / Data validation
* Pydantic (For all the data validation)
* Order matters (when creating path operations)

'''