from fastapi import FastAPI

from correction_adaptor.routers import languages, message
from correction_adaptor.exception_handlers import (
    http_error_handler,
    connection_error_handler,
)
from requests.exceptions import ConnectionError, HTTPError

app = FastAPI()

app.add_exception_handler(HTTPError, http_error_handler)
app.add_exception_handler(ConnectionError, connection_error_handler)

app.include_router(message.router)
app.include_router(languages.router)
