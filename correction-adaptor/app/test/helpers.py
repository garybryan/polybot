from functools import partial

from ..backends.base import Backend
from ..models import Message
from ..settings import BackendSettings

BASE_URL = "http://mock-backend"
SEND_MESSAGE_PATH = "fake-api/message"


class MockBackend(Backend):
    SEND_MESSAGE_PATH = "/message"

    def send_message(self, message: Message):
        pass


mock_backend_with_settings = partial(MockBackend, BackendSettings(base_url=BASE_URL))
