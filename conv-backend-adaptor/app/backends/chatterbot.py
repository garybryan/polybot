import requests

from config import BACKEND_CHATTERBOT
from models import Message
from .base import Backend

class ChatterbotBackend(Backend):
    def __init__(self, *args, **kwargs):
        self.URL = BACKEND_CHATTERBOT.URL

    def send_message(self, message: Message):
        response = requests.post(f'{BACKEND_CHATTERBOT.URL}/message', data=message.json())
        return Message.parse_obj(response.json())
