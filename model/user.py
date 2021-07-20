from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from data.config import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String)
    age = Column(Integer, default=20)
    password = Column(String)
    role = Column(String, default="normal")
    disable = Column(Boolean, default=False)
    todos = relationship("Todo", back_populates="owner")
