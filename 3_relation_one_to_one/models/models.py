from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, backref

from database import Base


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    father_name = Column(String)
    children = relationship("Child", uselist=False, back_populates="parent")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    child_name = Column(String)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")
