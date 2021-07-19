from sqlalchemy.orm import Session

from model import model
from schema import schemas


def create_todo(db: Session, current_user: model.User, todo_data: schemas.TODOCreate):
    todo = model.TODO(text=todo_data.text,
                      completed=todo_data.completed)
    todo.owner = current_user
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update_todo(db: Session, todo_data: schemas.TODOUpdate):
    todo = db.query(model.TODO).filter(model.TODO.id == id).first()
    todo.text = todo_data.text
    todo.completed = todo.completed
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, id: int):
    todo = db.query(model.TODO).filter(model.TODO.id == id).first()
    db.delete(todo)
    db.commit()


def get_user_todos(db: Session, userid: int):
    return db.query(model.TODO).filter(model.TODO.owner_id == userid).all()
