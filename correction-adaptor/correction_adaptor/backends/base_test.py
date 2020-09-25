from ..settings import BackendSettings
from ..test.helpers import MockBackend

BASE_URL = "http://mock-backend"
SEND_MESSAGE_PATH = "/message"


def test_base():
    settings = BackendSettings(base_url=BASE_URL)
    backend = MockBackend(settings)
    assert backend.send_message_url == f"{BASE_URL}{SEND_MESSAGE_PATH}"
