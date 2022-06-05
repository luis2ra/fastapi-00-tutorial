from sqlalchemy.orm import Session

from models import models
from schemas import user_schema, item_schema


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: item_schema.ItemCreate, user_id: int):
    # db_item = models.Item(**item.dict(), owner_id=user_id)
    db_item = models.Item(
        title = item.title,
        description = item.description,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    print('db_item', db_item.id)
    db_association = models.AssociationTable(
        user_id = user_id,
        item_id = db_item.id
    )
    db.add(db_association)
    db.commit()
    return db_item