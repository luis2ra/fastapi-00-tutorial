from typing import List, Optional

from pydantic import BaseModel
from schemas.item_schema import Item


class AssociationTableItems(BaseModel):
    user_id: int
    item_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[AssociationTableItems] = []

    class Config:
        orm_mode = True
