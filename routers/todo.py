from fastapi import APIRouter, Depends, HTTPException, status
from schema.todo import CreateTodo
from sqlalchemy.orm import Session
from data.config import get_db
from model.user import *
from model.todo import *
from schema.token import get_current_user
from schema.user import CurrentUser

todo_router = APIRouter(tags=["todo"])


@todo_router.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(request: CreateTodo, db: Session = Depends(get_db),
                currente_user: CurrentUser = Depends(get_current_user)
                ):
    me = db.query(User).filter(User.email == currente_user.email).first()
    todos = db.query(Todo).filter(Todo.title == request.title).all()
    if len(todos) > 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="there is already a whole with this title!"
        )
    Me_todo = Todo(
        title=request.title,
        todo_body=request.body,
        user_id=me.user_id
    )
    db.add(Me_todo)
    db.commit()
    db.refresh(Me_todo)

    return Me_todo
