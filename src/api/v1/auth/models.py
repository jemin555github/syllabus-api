from sqlalchemy import Column, Integer, String
from database.base import Base

class User(Base):
    __tablename__ = 'user_data'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(100), nullable=False)


