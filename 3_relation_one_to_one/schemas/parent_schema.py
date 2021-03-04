from typing import List, Optional

from pydantic import BaseModel
from schemas.child_schema import Child


class ParentBase(BaseModel):
    father_name: str


class ParentCreate(ParentBase):
    pass


class Parent(ParentBase):
    id: int
    child: List[Child] = []

    class Config:
        orm_mode = True
