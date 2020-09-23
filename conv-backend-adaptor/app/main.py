from asyncio import coroutine
from fastapi import FastAPI

import config

from models import Message
from message.post import post

app = FastAPI()


@app.post("/message")
def post_message(message: Message):
    return post(message)
