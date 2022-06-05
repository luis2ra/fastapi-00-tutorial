from sqlalchemy.orm import Session

from models import models
from schemas import parent_schema, child_schema


def get_parents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Parent).offset(skip).limit(limit).all()

    
def get_parent(db: Session, parent_id: int):
    return db.query(models.Parent).filter(models.Parent.id == parent_id).first()


def create_parent(db: Session, parent: parent_schema.ParentCreate):
    db_parent = models.Parent(
        father_name=parent.father_name,
        child_id=parent.child_id
    )
    db.add(db_parent)
    db.commit()
    db.refresh(db_parent)
    return db_parent


def get_childs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Child).offset(skip).limit(limit).all()


def get_child(db: Session, child_id: int):
    return db.query(models.Child).filter(models.Child.id == child_id).first()


def create_child(db: Session, child: child_schema.ChildCreate):
    db_child = models.Child(
        child_name = child.child_name
    )
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child