from typing import List, Optional

from pydantic import BaseModel


class ParentBase(BaseModel):
    father_name: str


class ParentCreate(ParentBase):
    child_id: int


class Parent(ParentBase):
    id: int
    child_id: int

    class Config:
        orm_mode = True
