import requests

from config import BACKEND_ECHO
from models import Message
from .base import Backend


class EchoBackend(Backend):
    URL = BACKEND_ECHO.URL
    SEND_MESSAGE_URL = f"{URL}/message"

    def send_message(self, message: Message):
        response = requests.post(self.SEND_MESSAGE_URL, json=message.dict())
        return Message.parse_obj(response.json())
