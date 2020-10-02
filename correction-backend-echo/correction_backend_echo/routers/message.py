from fastapi import APIRouter

from ..models import Message


router = APIRouter()


@router.post("/message")
def post(message: Message) -> Message:
    return Message(text=f"You said: {message.text}", langauge="en-GB")
