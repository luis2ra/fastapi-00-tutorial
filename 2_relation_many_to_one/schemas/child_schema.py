from typing import List, Optional

from pydantic import BaseModel
from schemas.parent_schema import Parent


class ChildBase(BaseModel):
    child_name: str


class ChildCreate(ChildBase):
    pass


class Child(ChildBase):
    id: int
    parents: List[Parent] = []
    
    class Config:
        orm_mode = True
