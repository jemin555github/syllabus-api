from src.api.v1.medias.models import Media

class MediaCrud: 

    @staticmethod
    def add_media(media_data, db):
        created_media = Media(**media_data.model_dump())
        db.add(created_media)
        db.commit()
        db.refresh(created_media)
        return created_media

    