from pydantic import BaseModel
from .todo import ShowTodo
from typing import List


class UserScheme(BaseModel):
    name: str
    email: str
    age: int
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    age: int
    role: str

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    name: str
    email: str
    age: int


class CurrentUser(BaseModel):
    user_id: int
    email: str
    role: str


class ShowMe(BaseModel):
    name: str
    email: str
    age: int
    role: str
    todos: List[ShowTodo] = []
