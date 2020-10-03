from fastapi import APIRouter

from ..models import CorrectedMessage, Message


router = APIRouter()


@router.post(
    "/message",
    response_model=CorrectedMessage,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
)
def post(message: Message) -> CorrectedMessage:
    return CorrectedMessage(language=message.language or "en-US", corrections=[])
