from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from data.config import Base
from datetime import datetime


class Todo(Base):
    __tablename__ = "todos"

    todo_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    disable = Column(Boolean, default=False)
    title = Column(String(100))
    todo_body = Column(Text)
    status = Column(Integer, default=0)
    create_date = Column(DateTime, default=datetime.utcnow())
    updated_date = Column(DateTime, default=datetime.utcnow())
    owner = relationship("User", back_populates="todos")
