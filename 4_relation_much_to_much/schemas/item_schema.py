from typing import List, Optional

from pydantic import BaseModel
# from schemas.user_schema import User


class AssociationTableUsers(BaseModel):
    user_id: int
    item_id: int

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    users: List[AssociationTableUsers] = []

    class Config:
        orm_mode = True
