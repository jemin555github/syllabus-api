from sqlalchemy import Column, Integer, String, DateTime, func
from database.database import Base

class User(Base):
    __tablename__ = "users"

    unique_id = Column(String(10), primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    grade = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False, default="India")
    phone = Column(String(20), nullable=False, unique=True)
    language = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)  # Store hashed password
    role = Column(String(50), nullable=False, default="user")  # user/admin
    age_group = Column(String(50), nullable=True)  # ✅ New field
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
