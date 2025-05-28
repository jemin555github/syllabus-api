from pydantic import BaseModel, EmailStr, constr

class User(BaseModel):
    id: int
    name: str
    last_name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: constr(min_length=6)

class AddUser(BaseModel):

    email: EmailStr
    password: constr(min_length=6)
    first_name: str
    last_name: str
