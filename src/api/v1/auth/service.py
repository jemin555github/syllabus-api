from src.utils.response_utils import Response
from src.api.v1.auth.models import User
from fastapi.security import OAuth2PasswordBearer
from src.api.v1.auth.crud import UserCrud
from src.utils.tokenization import create_access_token
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy import or_
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

class AuthServices:

    @staticmethod
    def signup(user_data, db):
        email = user_data.email

        is_email = db.query(User).filter(User.email == email).first()
        if is_email:
            return Response(
                data=user_data.email,
                status_code=403,
                success=True,
                message='Email Already Present'
            ).send_success_response()

        saved_user = UserCrud.add_user(user_data, db)
        print('saved_user', saved_user.unique_id)
        #breakpoint()
        return Response(
            data={
                "Unique_ID": saved_user.unique_id,
                "Email": saved_user.email,
                'grade':saved_user.grade,
                "Created At": str(saved_user.created_at)  # Add this line
            },
            status_code=200,
            success=True,
            message='User Added..'
        ).send_success_response()

    @staticmethod
    def signin(user_data, db):
        user_id = user_data.user_id
        is_user_id = db.query(User).filter(or_(User.email == user_id, User.unique_id == user_id)).first()        
        if not is_user_id:
            return Response(
                data=user_data.user_id,
                status_code=404,
                success=True,
                message='Email or ID Not Present'
            ).send_success_response()
        is_verified, current_user = UserCrud.verify_user(user_data, db)
        if is_verified:
             return Response(
                data={'email':current_user.email,
                       "Unique_ID": current_user.unique_id,
                      'grade':current_user.grade},
                status_code=200,
                success=True,
                message='Login Successfull..'
            ).send_success_response()
        else:
            return Response(
                data=user_id,
                status_code=401,
                success=True,
                message='Wrong Password or credentials'
            ).send_success_response()

    @staticmethod
    def get_current_user(token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            print('payload', payload)
            email: str = payload.get("email")
            if email is None:
                raise credentials_exception
            return payload  # Or return user_id, or query DB for full user object
        except JWTError:
            raise credentials_exception
