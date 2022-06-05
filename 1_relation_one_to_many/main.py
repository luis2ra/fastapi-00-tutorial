from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import models
from schemas import parent_schema, child_schema
from cruds import crud
from database import SessionLocal, engine


# Create the database tables¶
models.Base.metadata.create_all(bind=engine)        # In a very simplistic way create the database tables


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/parents/", response_model=List[parent_schema.Parent])
def read_parents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    parents = crud.get_parents(db, skip=skip, limit=limit)
    return parents


@app.get("/parents/{parent_id}", response_model=parent_schema.Parent)
def read_parent(parent_id: int, db: Session = Depends(get_db)):
    db_parent = crud.get_parent(db, parent_id=parent_id)
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent not found")
    return db_parent


@app.post("/parents/", response_model=parent_schema.Parent)
def create_parent(parent: parent_schema.ParentCreate, db: Session = Depends(get_db)):
    db_parent = crud.create_parent(db, parent=parent)
    # if db_parent:
    #     raise HTTPException(status_code=400, detail="Parent already registered")
    return db_parent


@app.get("/childs/", response_model=List[child_schema.Child])
def read_childs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    childs = crud.get_childs(db, skip=skip, limit=limit)
    return childs


@app.post("/childs/", response_model=child_schema.Child)
def create_child(child: child_schema.ChildCreate, db: Session = Depends(get_db)):
    db_child = crud.create_child(db, child=child)
    # if db_child:
    #     raise HTTPException(status_code=400, detail="Child already registered")
    return db_child
