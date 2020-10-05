from correction_adaptor.exception_handlers import (
    http_error_handler,
    connection_error_handler,
)
from requests.exceptions import ConnectionError, HTTPError


def test_main(mocker):
    # include_router = mocker.patch("main.app.include_router")

    from main import app

    assert app.exception_handlers[HTTPError] == http_error_handler
    assert app.exception_handlers[ConnectionError] == connection_error_handler

    # include_router.assert_called_once_with()
    # TODO how to make this work?
