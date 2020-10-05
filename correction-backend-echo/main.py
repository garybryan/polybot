from fastapi import FastAPI

from correction_backend_echo.routers import message, languages

app = FastAPI()

app.include_router(message.router)
app.include_router(languages.router)
