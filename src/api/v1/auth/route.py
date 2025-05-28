from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from src.api.v1.auth.schema import AddUser, UserLogin
from src.api.v1.auth.service import AuthServices

auth_router = APIRouter()

@auth_router.post("/signup")
def signup(user : AddUser, db:Session = Depends(get_db)):
    return AuthServices.signup(user, db)

@auth_router.post("/signin")
def signin(user : UserLogin, db:Session = Depends(get_db)):
    return AuthServices.signin(user, db)