from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/add_users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_clave(db, clave=user.clave)

    if db_user:
        raise HTTPException(status_code=400, detail="ID already registered")
    return crud.create_user(db=db, user=user)


@app.get("/buscar_users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/buscar_users/{user_clave}", response_model=schemas.User)
def read_user(user_clave: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_clave=user_clave)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_clave}", response_model=schemas.User)
def delete_user(user_clave: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_clave)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"clave": user_clave}


@app.put("/update_user/{clave}", response_model=schemas.UserUpdate)
def update_user(clave: int, user_data: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, clave, user_data.dict())
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="User not found")