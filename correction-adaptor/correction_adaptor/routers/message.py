from fastapi import APIRouter

from ..models import CorrectedMessage, Message
from ..backends import get_backend


router = APIRouter()


@router.post("/message")
def post(message: Message) -> CorrectedMessage:
    backend = get_backend()
    return backend.send_message(message)
