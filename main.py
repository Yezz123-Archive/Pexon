import uvicorn
from fastapi import FastAPI
from data.config import *
from routers import *
from model.todo import *
from model.user import *

Base.metadata.create_all(engine)

app = FastAPI(
    title="Pexon-Rest-API",
    description="A full Rest-API for JSON response included Docker Contains.",
    version="1.0.0",
)

app.include_router(signup_router)
app.include_router(login_router)
app.include_router(user_router)
app.include_router(todo_router)


@app.get(path="/")
def index():
    return {"detail": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.0", port=8000)
