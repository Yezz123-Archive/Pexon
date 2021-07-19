from datetime import timedelta
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from starlette.status import HTTP_401_UNAUTHORIZED
from schema.hash import authenticate_user
from schema.jwt import create_access_token, decode_access_token
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from core import crud
from model import model
from schema import schemas
from data.database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth", auto_error=False)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/users", response_model=schemas.User)
def signup(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    """add new user"""
    user = crud.get_user_by_email(db, user_data.email)
    if user:
        raise HTTPException(status_code=409,
                            detail="Email already registered.")
    signedup_user = crud.create_user(db, user_data)
    return signedup_user


@app.post("/api/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db),
                           form_data: OAuth2PasswordRequestForm = Depends()):
    """generate access token for valid credentials"""
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.email},
                                       expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(db: Session = Depends(get_db),
                     token: str = Depends(oauth2_scheme)):
    return decode_access_token(db, token)


@app.get("/api/me", response_model=schemas.User)
def read_logged_in_user(current_user: model.User = Depends(get_current_user)):
    """return user settings for current user"""
    return current_user


@app.get("/api/mytodos", response_model=List[schemas.TODO])
def get_own_todos(current_user: model.User = Depends(get_current_user),
                  db: Session = Depends(get_db)):
    """return a list of TODOs owned by current user"""
    todos = crud.get_user_todos(db, current_user.id)
    return todos


@app.post("/api/todos", response_model=schemas.TODO)
def add_a_todo(todo_data: schemas.TODOCreate,
               current_user: model.User = Depends(get_current_user),
               db: Session = Depends(get_db)):
    """add a TODO"""
    todo = crud.create_meal(db, current_user)
    return todo


@app.put("/api/todos/{todo_id}", response_model=schemas.TODO)
def update_a_todo(todo_id: int,
                  todo_data: schemas.TODOUpdate,
                  current_user: model.User = Depends(get_current_user),
                  db: Session = Depends(get_db)):
    """update and return TODO for given id"""
    todo = crud.get_todo(db, todo_id)
    updated_todo = crud.update_todo(db, todo_id, todo_data)
    return updated_todo


@app.delete("/api/todos/{todo_id}")
def delete_a_meal(todo_id: int,
                  current_user: model.User = Depends(get_current_user),
                  db: Session = Depends(get_db)):
    """delete TODO of given id"""
    crud.delete_meal(db, todo_id)
    return {"detail": "TODO Deleted"}
