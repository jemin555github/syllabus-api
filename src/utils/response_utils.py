from typing import Any
from fastapi.responses import JSONResponse

class Response:
    """
    Return success and error response.
    """

    def __init__(self, status_code: int, success: bool, data: Any = None, message: str = None) -> None:
        self.status_code = status_code
        self.message = message
        self.data = data
        self.success = int(success)

    def send_success_response(self, kwargs=None):
        """
       Return success response with status RESPONSE_STATUS_SUCCESS
       :return: success response
       """
        if not kwargs:
            kwargs = {}
        return JSONResponse(
            content={
                "data": self.data,
                "meta": {
                    "code": self.success,
                    "message": self.message or "Success",
                    "status_code": self.status_code,
                    **kwargs
                }
            },
            status_code=self.status_code)

    def send_error_response(self, kwargs=None):
        """
        Return error response with status RESPONSE_STATUS_ERROR
        :return: error response
        """
        if not kwargs:
            kwargs = {}
        return JSONResponse(
            content={
                "data": self.data,
                "meta": {
                    "code": self.success,
                    "message": self.message or "Error",
                    "status_code": self.status_code,
                    **kwargs
                }
            },
            status_code=self.status_code)
