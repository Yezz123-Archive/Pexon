from passlib.context import CryptContext
from core import crud

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
 
def verify_password(plain_password, hashed_password):
   return pwd_context.verify(plain_password, hashed_password)
 
 
def get_password_hash(password):
   return pwd_context.hash(password)
 
def authenticate_user(db, email: str, password: str):
   user = crud.get_user_by_email(db, email)
   if not user:
   	return False
   if not verify_password(password, user.hashed_password):
   	return False
   return user