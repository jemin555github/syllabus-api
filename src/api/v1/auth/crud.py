from src.api.v1.auth.models import User
from src.utils.hashing import Hashing
import time


class UserCrud: 

    @staticmethod
    def add_user(user_data, db):
        hashed_password = Hashing.create_hash(user_data.password)
        age_group = UserCrud.get_age_group(user_data.age)
        state_prefix = user_data.state.replace(' ', '').upper()[:2]
        phone_digits = ''.join(filter(str.isdigit, user_data.phone))[-4:]
        timestamp_digits = str(int(time.time()))[-4:]
        unique_id = f"{state_prefix}{phone_digits}{timestamp_digits}"
        new_user = User(
            unique_id=unique_id,
            email=user_data.email,
            password=hashed_password,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            age=user_data.age,
            state=user_data.state,
            country=user_data.country,
            phone=user_data.phone,
            language=user_data.language,
            role=user_data.role,
            age_group=age_group,
            grade=user_data.grade,

        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def verify_user(user_data, db):
        current_user = db.query(User).filter(User.email == user_data.user_id).first()
        hashed_password = current_user.password
        return Hashing.verify_hash(user_data.password, hashed_password), current_user

    @staticmethod
    def get_age_group(age: int):
        if age <= 12:
            return "child"
        elif 13 <= age <= 19:
            return "teenager"
        else:
            return "man"
