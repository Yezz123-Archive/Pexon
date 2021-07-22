from fastapi import APIRouter, Depends, HTTPException, status
from schema.user import UserScheme, ShowUser
from sqlalchemy.orm import Session
from data.config import get_db, pwd_context
from model.user import *

signup_router = APIRouter(tags=["Signup"])


@signup_router.post("/Register",
                   status_code=status.HTTP_201_CREATED,
                   response_model=ShowUser)
async def create_user(request: UserScheme, db: Session = Depends(get_db)):
    new_user = User(name=request.name,
                    email=request.email.lower(),
                    age=request.age,
                    password=pwd_context.hash(request.password),
                    role="normal"
                    )

    if not db.query(User).first():
        new_user.role = "admin"

    if db.query(User).filter(User.email == request.email).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="the email {} already exists!".format(request.email)
        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
