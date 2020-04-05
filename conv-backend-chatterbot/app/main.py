from fastapi import FastAPI
from pydantic import BaseModel

from chatbot import chatbot

app = FastAPI()
print("APP READY")

@app.get("/")
def read_root():
    return {"Hello": "World"}


class Message(BaseModel):
    text: str


@app.post("/message")
async def post_message(message: Message):
    response = chatbot.get_response(message.text)
    return Message(text=str(response))

