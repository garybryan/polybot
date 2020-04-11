from abc import ABC, abstractmethod

from models import Message

class Backend(ABC):
    @abstractmethod
    def send_message(self, message: Message):
        pass
