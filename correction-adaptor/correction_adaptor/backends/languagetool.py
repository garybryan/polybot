import requests

from ..models import Message
from .base import Backend


class LanguageToolBackend(Backend):
    def send_message(self, message: Message):
        response = requests.post(self.send_message_url, json=message.dict())
        return Message.parse_obj(response.json())
