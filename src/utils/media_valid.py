import mimetypes
from fastapi import UploadFile
from src.utils.response_utils import Response  # Your custom response class
from src.api.v1.medias.models import MediaTypeEnum  # Your media type enum

class MediaValidation:
    def validate_media_request_data(media_input, media_type: MediaTypeEnum):
        """
        Validate media type (video, image, document, etc.) based on the input.
        
        Parameters:
            media_input: str (URL) or UploadFile
            media_type: MediaTypeEnum

        Returns:
            - JSONResponse (success) if valid
            - JSONResponse (error) if invalid
        """
        # Guess MIME type from URL or UploadFile
        if isinstance(media_input, str):
            mime_type, _ = mimetypes.guess_type(media_input)
        elif isinstance(media_input, UploadFile):
            mime_type = media_input.content_type
        else:
            return Response(
                status_code=400,
                success=False,
                message="Invalid media input type",
                data=None
            ).send_error_response()

        if not mime_type:
            return Response(
                status_code=400,
                success=False,
                message="Unable to determine media type",
                data=None
            ).send_error_response()

        # Match against expected media_type
        if media_type == MediaTypeEnum.image and mime_type.startswith("image/"):
            pass
        elif media_type == MediaTypeEnum.video and mime_type.startswith("video/"):
            pass
        elif media_type == MediaTypeEnum.document and (
            mime_type.startswith("application/") or mime_type in ["text/plain", "text/html"]
        ):
            pass
        elif media_type == MediaTypeEnum.audio and mime_type.startswith("audio/"):
            pass
        elif media_type == MediaTypeEnum.other:
            pass
        else:
            return Response(
                status_code=400,
                success=False,
                message=f"Media type mismatch: expected {media_type}, got {mime_type}",
                data=None
            ).send_error_response()

        # Success response (you can customize `data` if needed)
        return Response(
            status_code=200,
            success=True,
            message="Media validated successfully",
            data={"mime_type": mime_type}
        ).send_success_response()
