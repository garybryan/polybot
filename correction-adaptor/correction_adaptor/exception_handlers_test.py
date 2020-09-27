import json
from requests import Response
from requests.exceptions import HTTPError

from .exception_handlers import http_error_handler, connection_error_handler


def test_http_error_handler(mocker):
    Request = mocker.patch("fastapi.Request")

    response = Response()
    response.status_code = 404

    error = HTTPError("Not Found", response=response)
    handler_response = http_error_handler(Request(), error)

    assert handler_response.status_code == 404
    assert json.loads(handler_response.body) == {"message": "Not Found"}


def test_connection_error_handler(mocker):
    Request = mocker.patch("fastapi.Request")

    error = ConnectionError("Unable to connect")
    handler_response = connection_error_handler(Request(), error)

    assert handler_response.status_code == 502
    assert json.loads(handler_response.body) == {"message": "Unable to connect"}
