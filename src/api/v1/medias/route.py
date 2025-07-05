from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.api.v1.medias.models import Media
from src.api.v1.medias.schema import MediaCreate
from src.api.v1.medias.service import MediaServices
from database.database import get_db
from fastapi import Query
from typing import List
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/facebook-meta-ads/signin")  # or whatever your signin path is

media_router = APIRouter()

@media_router.post("/media")
def add_media(media_data: MediaCreate, db: Session = Depends(get_db)):
    return MediaServices.add_media(media_data, db)

@media_router.get("/media-file")
def get_media(id: int = Query(None), db: Session = Depends(get_db)):
    return MediaServices.get_media(db=db, id=id)

@media_router.get("/media-file/by-age-group")
def get_media_by_group(groups: List[str] = Query(...), db: Session = Depends(get_db)):
    """
    Example: /media-file/by-age-group?groups=child&groups=man
    """
    return MediaServices.get_media_by_age_groups(groups, db)

@media_router.get("/media-file/by-user")
def get_media_by_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return MediaServices.get_media_for_user(token, db)

