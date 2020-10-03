from fastapi import APIRouter

from ..models import CorrectedMessage, Message
from ..backends import get_backend


router = APIRouter()


@router.post(
    "/message", response_model=CorrectedMessage, response_model_exclude_none=True
)
def post(message: Message) -> CorrectedMessage:
    backend = get_backend()
    reply = backend.send_message(message)
    return reply
