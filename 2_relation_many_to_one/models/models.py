from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, backref

from database import Base


# # Simple relation Many To One
# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     father_name = Column(String)
#     child_id = Column(Integer, ForeignKey('child.id'))
#     child = relationship("Child")


# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     child_name = Column(String)


# Bidirectional behavior is achieved by adding a second relationship() 
# and applying the relationship.back_populates parameter in both directions:
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    father_name = Column(String)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", back_populates="parents")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    child_name = Column(String)
    parents = relationship("Parent", back_populates="child")