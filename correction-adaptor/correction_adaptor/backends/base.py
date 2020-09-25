from abc import ABC, abstractmethod

from ..settings import BackendSettings
from ..models import Message


class Backend(ABC):
    SEND_MESSAGE_PATH = "/message"

    def __init__(self, settings: BackendSettings):
        self.settings = settings

    @property
    def send_message_url(self):
        return f"{self.settings.base_url}{self.SEND_MESSAGE_PATH}"

    @abstractmethod
    def send_message(self, message: Message):
        pass
