from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel
from data.config import get_db, pwd_context, Oauth2_scheme
from model.user import *
from schema.token import create_access_token

login_router = APIRouter(tags=["Token"], include_in_schema=False)


@login_router.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    login_user = db.query(User).filter(request.username == User.email).first()
    if not login_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="{} does not exist".format(request.username)
                            )
    if not pwd_context.verify(request.password, login_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="incorrect password"
                            )
    token = create_access_token(data={"sub": login_user.email,
                                      "id": login_user.user_id,
                                      "role": login_user.role
                                      })

    return {"access_token": token, "token_type": "bearer"}


