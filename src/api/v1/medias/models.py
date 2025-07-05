from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from sqlalchemy.sql import func
from database.database import Base
from src.api.v1.medias.schema import MediaTypeEnum  # Assuming you save the enum here
from sqlalchemy.dialects.postgresql import ARRAY  # ✅ Import ARRAY from PostgreSQL

class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    media_id = Column(String(150), nullable=False, unique=True)
    media_link = Column(Text, nullable=False)
    media_type = Column(String(50), nullable=False)  # removed Enum
    title = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    age_group = Column(ARRAY(String), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())