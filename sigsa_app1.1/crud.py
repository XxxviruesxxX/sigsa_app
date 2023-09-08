from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_clave: int):
    return db.query(models.User).filter(models.User.clave == user_clave).first()


def get_user_by_clave(db: Session, clave: str):
    return db.query(models.User).filter(models.User.clave == clave).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        clave=user.clave,
        nombre=user.nombre,
        jefe_directo=user.jefe_directo,
        departamento=user.departamento,
        fecha_ingreso=user.fecha_ingreso,
        antiguedad =user.antiguedad,
        is_active=user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_clave: int):
    user = db.query(models.User).filter(models.User.clave == user_clave).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

def update_user(db: Session, clave: int, user_data: dict):
    db_user = db.query(models.User).filter(
        models.User.clave == clave).first()
    if db_user:
        for field, value in user_data.items():
            setattr(db_user, field, value)
        db.commit()
        db.refresh(db_user)
        return db_user
    return None






