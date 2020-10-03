from correction_adaptor.backends.languagetool.mapping import map_message
import pytest
from requests.exceptions import HTTPError

from ...models import CorrectedMessage, Message
from ...settings import BackendSettings
from .languagetool import LanguageToolBackend
from .models import LanguageToolCorrectedMessage, LanguageToolMessage


@pytest.fixture
def backend():
    return LanguageToolBackend(BackendSettings(base_url="http://backend-languagetool/"))


def test_send_message(mocker, backend):
    map_message = mocker.patch(
        "correction_adaptor.backends.languagetool.languagetool.map_message"
    )
    map_corrected_message = mocker.patch(
        "correction_adaptor.backends.languagetool.languagetool.map_corrected_message"
    )
    post = mocker.patch("requests.post")

    message = Message(text="test")
    lt_message = LanguageToolMessage(text="test", motherTongue="en-GB")
    map_message.return_value = lt_message

    url = backend.send_message_url

    reply = LanguageToolCorrectedMessage(text="reply", language="en-US", matches=[])
    post.return_value.json.return_value = reply

    corrected_message = CorrectedMessage(text="reply", language="en-US", corrections=[])
    map_corrected_message.return_value = corrected_message

    result = backend.send_message(message)

    map_message.assert_called_once_with(message)
    post.assert_called_once_with(url, json=lt_message.dict())
    map_corrected_message.assert_called_once_with(reply)
    assert result == corrected_message


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
