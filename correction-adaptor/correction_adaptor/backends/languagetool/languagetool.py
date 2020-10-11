from typing import List
import requests

from ...models import CorrectedMessage, Language, Message
from ..base import Backend
from .models import LanguageToolCorrectedMessage
from .mapping import map_corrected_message, map_message


class LanguageToolBackend(Backend):
    SEND_MESSAGE_PATH = "/check"

    def send_message(self, message: Message) -> CorrectedMessage:
        lt_message = map_message(message)
        response = requests.post(
            self.send_message_url,
            data=lt_message.dict(exclude_unset=True, exclude_none=True),
        )
        response.raise_for_status()
        print("RESPONSE", response.json())
        corrected_message = LanguageToolCorrectedMessage.parse_obj(response.json())
        return map_corrected_message(corrected_message)

    def parse_supported_languages(self, languages: List[dict]) -> List[Language]:
        return [
            Language(code=language["longCode"], name=language["name"])
            for language in languages
        ]
