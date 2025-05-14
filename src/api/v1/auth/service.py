from src.utils.response_utils import Response
from src.api.v1.auth.models import User
from src.api.v1.auth.crud import UserCrud

from src.utils.hashing import Hashing

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

        is_verified = UserCrud.verify_user(user_data, db)
        if is_verified:
            return Response(
                    data=email,
                    status_code=200,
                    success=True,
                    message='Password Verified'
                ).send_success_response()
        else:
            return Response(
                data=email,
                status_code=403,
                success=True,
                message='Wrong Password'
            ).send_success_response()