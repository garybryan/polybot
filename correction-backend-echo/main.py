from fastapi import FastAPI

from correction_backend_echo.routers import message

app = FastAPI()

app.include_router(message.router)
