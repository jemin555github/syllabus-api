from src.utils.response_utils import Response
from src.api.v1.auth.models import User
from fastapi.security import OAuth2PasswordBearer
from src.api.v1.auth.crud import UserCrud
from src.utils.tokenization import create_access_token
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
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
                status_code=200,
                success=True,
                message='Email Already Present'
            ).send_success_response()

        saved_user = UserCrud.add_user(user_data, db)

        return Response(
                data={"Id":saved_user.id, "Email": saved_user.email},
                status_code=200,
                success=True,
                message='User Added..'
            ).send_success_response()

    @staticmethod
    def signin(user_data, db):
        email = user_data.email

        is_email = db.query(User).filter(User.email == email).first()
        if not is_email:
            return Response(
                data=user_data.email,
                status_code=404,
                success=True,
                message='Email Not Present'
            ).send_success_response()

        is_verified, current_user = UserCrud.verify_user(user_data, db)
        if is_verified:
            user_data_dict = {"email":current_user.email, "id":current_user.id}
            token = create_access_token(user_data_dict)
            current_user = AuthServices.get_current_user(token)
            return Response(
                    data={"token":token, 'user_data':current_user},
                    status_code=200,
                    success=True,
                    message='Auth Succeed'
                ).send_success_response()
        else:
            return Response(
                data=email,
                status_code=403,
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
