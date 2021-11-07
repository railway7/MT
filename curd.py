from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, id: int):
    return db.query(models.user).filter(models.user.id == id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.user).filter(models.user.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.user).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.Createuser):
    db_user = models.user(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_by_code(db: Session, user):
    db_user = models.user(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def change_user_by_code(db: Session, user):
    db_user = models.user(**user)
    mod_user = db.query(models.user).filter(models.user.name == db_user.name).first()
    models.user.pushPlusToken = db_user.pushPlusToken
    mod_user.wm_latitude = db_user.wm_latitude
    mod_user.wm_longitude = db_user.wm_longitude
    mod_user.propId = db_user.propId
    mod_user.exchangeCoinNumber = db_user.exchangeCoinNumber
    mod_user.token = db_user.token
    db.commit()
    db.refresh(mod_user)
    return mod_user


def delete_user_by_code(db: Session, name: str):
    mod_user = db.query(models.user).filter(models.user.name == name).first()
    db.delete(mod_user)
    db.commit()
    return mod_user