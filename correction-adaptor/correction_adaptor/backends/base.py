import requests

from abc import ABC, abstractmethod
from functools import cached_property
from typing import Any, List

from ..settings import BackendSettings
from ..models import CorrectedMessage, Message, Language


class Backend(ABC):
    SEND_MESSAGE_PATH = "/message"
    SUPPORTED_LANGUAGES_PATH = "/languages"

    def __init__(self, settings: BackendSettings):
        self.settings = settings

    @property
    def send_message_url(self) -> str:
        return f"{self.settings.base_url}{self.SEND_MESSAGE_PATH}"

    @property
    def supported_languages_url(self) -> str:
        return f"{self.settings.base_url}{self.SUPPORTED_LANGUAGES_PATH}"

    @cached_property
    def supported_languages(self) -> List[Language]:
        return self.get_supported_languages()

    def parse_supported_languages(self, languages: Any) -> List[Language]:
        return [Language.parse_obj(language) for language in languages]

    def get_supported_languages(self) -> List[Language]:
        response = requests.get(self.supported_languages_url)
        response.raise_for_status()
        return self.parse_supported_languages(response.json())

    @abstractmethod
    def send_message(self, message: Message) -> CorrectedMessage:
        pass
