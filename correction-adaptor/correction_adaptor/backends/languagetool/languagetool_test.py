import pytest
from requests.exceptions import HTTPError

from ...models import Message
from ...settings import BackendSettings
from .languagetool import LanguageToolBackend


@pytest.fixture
def backend():
    return LanguageToolBackend(BackendSettings(base_url="http://backend-languagetool/"))


def test_send_message(mocker, backend):
    post = mocker.patch("requests.post")

    message = Message(text="test")
    url = backend.send_message_url

    reply = Message(text="reply")
    post.return_value.json.return_value = reply

    result = backend.send_message(message)

    post.assert_called_once_with(url, json=message.dict())
    assert result == reply


def test_send_message_connection_error(mocker, backend):
    post = mocker.patch("requests.post")

    message = Message(text="test")

    post.side_effect = ConnectionError()

    with pytest.raises(ConnectionError):
        backend.send_message(message)


def test_send_message_http_error(mocker, backend):
    post = mocker.patch("requests.post")
    post.return_value.raise_for_status.side_effect = HTTPError()

    message = Message(text="test")

    with pytest.raises(HTTPError):
        backend.send_message(message)
