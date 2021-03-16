#!/usr/bin/env python
import json
from typing import List, Optional
from fastapi import FastAPI, Query, Path, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic.types import JsonMeta
from odmantic import AIOEngine, Model, ObjectId
from model.model import TodoItem

app = FastAPI()
with open('todos.json') as f:
    TODOS = json.load(f)
engine = AIOEngine()

@app.exception_handler(Exception)
async def error_handler(request, exc):
    return JSONResponse({
        'detail': f'{exc}'
    })

@app.get('/todos',tags=['todos'],response_model=List[TodoItem])
async def get_todos(limit: int = Query(None, le=100)):
        return TODOS[0:limit]

@app.get('/todos/{id}',tags=['todos'], response_model=TodoItem)
async def get_todo(todo_id: int=Path(...)):
    try:
        return TODOS[todo_id - 1]
    except IndexError:
        raise HTTPException(404, 'Todo not found')

@app.post('/todos', tags=['todos'],status_code=201, response_model=TodoItem)
async def create_todo(todo: TodoItem):
    item = todo.dict()
    item['id'] = len(TODOS) +1
    return item

@app.put('/todos/{id}', tags=['todos'], response_model=TodoItem)
async def update_todo(todo_id: int, todo: TodoItem, q: Optional[str] = None):
    result = {"todo_id": todo_id, **todo.dict()}
    if q:
        result.update({"q": q})
    return result

@app.delete('/todos/{id}', tags=['todos'], response_model=TodoItem)
async def delete_todo(todo_id: int, response_model=TodoItem):
    todo_id = JsonMeta = [""]
    todo = await engine.find_one(TodoItem, TodoItem.id == id)
    if todo is None:
        raise HTTPException(404)
    await engine.delete(todo)
    return todo