# pydantic : pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
from pydantic import BaseModel, Schema

class TodoItem(BaseModel):
    title: str = Schema(..., description='Name of todo item', max_length=180)