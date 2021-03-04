from sqlalchemy.orm import Session

#from . import models, schemas
from models import models
from schemas import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(user_id: int, user: schemas.UserUpdate, db: Session):
    db.query(models.User).filter(models.User.id == user_id).update({
        'is_active': user.is_active,
        'email': user.email
    })
    db.commit()

    return db.query(models.User).filter(models.User.id == user_id).first()


def delete_user(user_id: int, db: Session):
    if db.query(models.User).filter(models.User.id == user_id).count():
        user = db.query(models.User).filter(models.User.id == user_id).first()
        db.delete(user)
        db.commit()

        return "deleted record"
    return "no exist record with id equal to " + str(user_id)


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).filter(models.Item.owner_id != None).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item