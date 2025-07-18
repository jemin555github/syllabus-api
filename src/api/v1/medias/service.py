from src.utils.response_utils import Response
from src.api.v1.medias.models import Media
from src.api.v1.auth.models import User
from src.api.v1.auth.service import AuthServices
from fastapi.security import OAuth2PasswordBearer
from src.api.v1.medias.crud import MediaCrud
from src.utils.tokenization import create_access_token
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from src.utils.media_valid import MediaValidation


class MediaServices:

    @staticmethod
    def add_media(media_data, db):
        MediaValidation.validate_media_request_data(media_data.media_link, media_data.media_type)
        media = MediaCrud.add_media(media_data=media_data, db=db)
        return Response(
            data={
                "Id": media.id,
                "Media_link": media.media_link,
                "Created At": str(media.created_at)  # Add this line
            },
            status_code=200,
            success=True,
            message='Media Added..'
        ).send_success_response()

    def get_media(db, id=None):
        if id:
            media = db.query(Media).filter(Media.id == id).first()
            if not media:
                return Response(
                    data=None,
                    status_code=404,
                    success=False,
                    message="Media not found"
                ).send_error_response()

            return Response(
                data={
                    "id": media.id,
                    "media_id": media.media_id,
                    "media_link": media.media_link,
                    "media_type": media.media_type,
                    "title": media.title,
                    "description": media.description,
                    "created_at": str(media.created_at)
                },
                status_code=200,
                success=True,
                message="Media fetched successfully"
            ).send_success_response()
        else:
            media_list = db.query(Media).all()
            media_data = [
                {
                    "id": m.id,
                    "media_id": m.media_id,
                    "media_link": m.media_link,
                    "media_type": m.media_type,
                    "title": m.title,
                    "description": m.description,
                    "created_at": str(m.created_at)
                }
                for m in media_list
            ]

            return Response(
                data=media_data,
                status_code=200,
                success=True,
                message="All media fetched successfully"
            ).send_success_response()

    @staticmethod
    def get_media_by_age_groups(groups: list[str], db):
        if not groups:
            return Response(
                data=None,
                status_code=400,
                success=False,
                message="No age group provided"
            ).send_error_response()

        media_list = db.query(Media).filter(
            Media.age_group.overlap(groups)  # Works now
        ).all()

        if not media_list:
            return Response(
                data=[],
                status_code=200,
                success=True,
                message="No media found for given age group(s)"
            ).send_success_response()

        media_data = [
            {
                "id": m.id,
                "media_id": m.media_id,
                "media_link": m.media_link,
                "media_type": m.media_type,
                "title": m.title,
                "description": m.description,
                "age_group": m.age_group,
                "created_at": str(m.created_at)
            }
            for m in media_list
        ]

        return Response(
            data=media_data,
            status_code=200,
            success=True,
            message="Media fetched for given age group(s)"
        ).send_success_response()


    @staticmethod
    def get_media_for_user(token, db):
        user_data = AuthServices.get_current_user(token)
        user_unique_id = user_data.get("unique_id")
        user = db.query(User).filter(User.unique_id == user_unique_id).first()
        if not user:
            return Response(
                data=None,
                status_code=404,
                success=False,
                message="User not found"
            ).send_error_response()

        age_group = user.age_group
        media_list = db.query(Media).filter(
            Media.age_group.overlap([age_group])
        ).all()

        media_data = [
            {
                "id": m.id,
                "media_id": m.media_id,
                "media_link": m.media_link,
                "media_type": m.media_type,
                "title": m.title,
                "description": m.description,
                "age_group": m.age_group,
                "created_at": str(m.created_at)
            }
            for m in media_list
        ]

        return Response(
            data=media_data,
            status_code=200,
            success=True,
            message=f"Media for age group: {age_group}"
        ).send_success_response()
