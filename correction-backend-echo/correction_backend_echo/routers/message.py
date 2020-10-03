from fastapi import APIRouter

from ..models import Message


router = APIRouter()


@router.post(
    "/message", response_model=CorrectedMessage, response_model_
)
def post(message: Message) -> Message:
    return Message(text=f"You said: {message.text}", language="en-GB")
