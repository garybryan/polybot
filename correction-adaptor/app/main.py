from fastapi import FastAPI

from .routers import message

app = FastAPI()

app.include_router(message.router)

from .settings import Settings

print(Settings().dict())
