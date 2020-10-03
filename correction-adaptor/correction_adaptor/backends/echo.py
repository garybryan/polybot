import requests

from ..models import CorrectedMessage, Message
from .base import Backend


class EchoBackend(Backend):
    def send_message(self, message: Message) -> CorrectedMessage:
        response = requests.post(
            self.send_message_url,
            json=message.dict(exclude_unset=True, exclude_none=True),
        )
        response.raise_for_status()
        return CorrectedMessage.parse_obj(response.json())
