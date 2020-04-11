import requests

from config import BACKEND_CHATTERBOT
from models import Message
from .base import Backend

class ChatterbotBackend(Backend):
    URL = BACKEND_CHATTERBOT.URL
    SEND_MESSAGE_URL = f'{URL}/message'

    def send_message(self, message: Message):
        print('posting', self.SEND_MESSAGE_URL)
        response = requests.post(self.SEND_MESSAGE_URL, json=message.dict())
        return Message.parse_obj(response.json())
