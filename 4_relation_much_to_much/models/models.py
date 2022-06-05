from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from database import Base


class AssociationTable(Base):
    __tablename__ = "association"
    
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)
    user = relationship("User", back_populates="items")
    item = relationship("Item", back_populates="users")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship(
        "AssociationTable", 
        back_populates="user"
    )


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    users = relationship(
        "AssociationTable",
        back_populates="item"
    )
