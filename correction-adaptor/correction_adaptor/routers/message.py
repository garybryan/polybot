from fastapi import APIRouter
from functools import wraps

from ..models import Message
from ..backends import get_backend


router = APIRouter()


@router.post("/message")
def post(message: Message):
    backend = get_backend()
    reply = backend.send_message(message)
    return reply
