from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from src.api.v1.auth import models
from src.api.v1.medias import models
