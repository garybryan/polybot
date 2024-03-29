import pytest
from requests.exceptions import ConnectionError, HTTPError

from ..models import CorrectedMessage, Message
from ..settings import BackendSettings
from .echo import EchoBackend


MESSAGE = Message(text="test", language="en-GB")


@pytest.fixture
def backend() -> EchoBackend:
    return EchoBackend(BackendSettings(base_url="http://backend-echo/"))


def test_send_message(mocker, backend):
    post = mocker.patch("requests.post")

    message = Message(text="ça va ?", language="fr")
    url = backend.send_message_url

    reply = CorrectedMessage(language="fr", corrections=[])
    post.return_value.json.return_value = reply

    result = backend.send_message(message)

    post.assert_called_once_with(
        url, json=message.dict(exclude_unset=True, exclude_none=True)
    )
    assert result == reply


def test_send_message_connection_error(mocker, backend):
    post = mocker.patch("requests.post")

    post.side_effect = ConnectionError()

    with pytest.raises(ConnectionError):
        backend.send_message(MESSAGE)


def test_send_message_http_error(mocker, backend):
    post = mocker.patch("requests.post")
    post.return_value.raise_for_status.side_effect = HTTPError()

    with pytest.raises(HTTPError):
        backend.send_message(MESSAGE)