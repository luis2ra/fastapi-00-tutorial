from typing import List, Optional

from pydantic import BaseModel
# from schemas.user_schema import User


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    # owners: List[User] = []

    class Config:
        orm_mode = True
