from typing import List, Optional

from pydantic import BaseModel


class ChildBase(BaseModel):
    child_name: str


class ChildCreate(ChildBase):
    pass
    #parent_id: int


class Child(ChildBase):
    id: int
    #parent_id: int
    
    class Config:
        orm_mode = True
