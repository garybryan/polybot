import requests

from ..models import Message
from .base import Backend


class LanguageToolBackend(Backend):
    def send_message(self, message: Message):
        response = requests.post(self.send_message_url, json=message.dict())
        response.raise_for_status()
        return Message.parse_obj(response.json())
