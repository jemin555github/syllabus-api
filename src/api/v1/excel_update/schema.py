from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, List
from enum import Enum


class MediaTypeEnum(str, Enum):
    video = "video"
    image = "image"
    document = "document"
    audio = "audio"
    other = "other"

class MediaCreate(BaseModel):
    media_id: str
    media_link: str
    media_type: str  # simple string now
    title: Optional[str] = None
    description: Optional[str] = None
    age_group: List[str] = Field(..., min_items=1)

