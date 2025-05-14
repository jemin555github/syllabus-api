from wsgiref.util import request_uri

from src.api.v1.auth.models import User
from src.utils.hashing import Hashing


class UserCrud:

    @staticmethod
    def add_user(user_data, db):
        hashed_password = Hashing.create_hash(user_data.password)
        new_user = User(
            email=user_data.email,
            password=hashed_password,
            name=user_data.first_name,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def verify_user(user_data, db):
        current_user = db.query(User).filter(User.email == user_data.email).first()
        hashed_password = current_user.password

        return Hashing.verify_hash(user_data.password, hashed_password)
