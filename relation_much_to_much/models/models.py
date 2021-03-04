from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from database import Base


association_table = Table('association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('item_id', Integer, ForeignKey('items.id'))
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship(
        "Item", 
        secondary=association_table,
        back_populates="owners"
    )


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    # owner_id = Column(Integer, ForeignKey("users.id"))

    owners = relationship(
        "User",
        secondary=association_table,
        back_populates="items"
    )
