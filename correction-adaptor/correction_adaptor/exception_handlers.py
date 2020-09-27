from requests.exceptions import HTTPError
from fastapi import Request
from fastapi.responses import JSONResponse


def _make_error_response(message: str, status_code: int):
    return JSONResponse(status_code=status_code, content={"message": message})


def http_error_handler(request: Request, exc: HTTPError):
    return _make_error_response(str(exc), exc.response.status_code)


def connection_error_handler(request: Request, exc: HTTPError):
    return _make_error_response(str(exc), 502)
