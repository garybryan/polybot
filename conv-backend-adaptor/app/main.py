from fastapi import FastAPI
from models import Message
from backends import BACKENDS

import config

app = FastAPI()

backend = BACKENDS[config.BACKEND]()

@app.post("/message")
async def post_message(message: Message):
    reply = backend.send_message(message)
    # TODO make this async
    return reply

