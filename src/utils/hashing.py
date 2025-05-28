from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hashing:

    @staticmethod
    def create_hash(plain_str):
        return pwd_context.hash(plain_str)

    @staticmethod
    def verify_hash(plain_str, hashed_str):
        return pwd_context.verify(plain_str, hashed_str)

