import requests

from ...models import CorrectedMessage, Message
from ..base import Backend
from .models import LanguageToolCorrectedMessage
from .mapping import map_corrected_message, map_message


class LanguageToolBackend(Backend):
    SEND_MESSAGE_PATH = "/check"

    def send_message(self, message: Message) -> CorrectedMessage:
        lt_message = map_message(message)
        print("sending message", message, lt_message)
        response = requests.post(self.send_message_url, json=lt_message.dict())
        response.raise_for_status()
        # corrected_message = LanguageToolCorrectedMessage.parse_obj(response.json())
        corrected_message = LanguageToolCorrectedMessage.parse_obj(response.json())
        return map_corrected_message(corrected_message)
