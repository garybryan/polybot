import pytest
from requests.exceptions import ConnectionError, HTTPError

from ...models import CorrectedMessage, Message
from ...settings import BackendSettings
from .languagetool import LanguageToolBackend
from .models import (
    LanguageToolCorrectedMessage,
    LanguageToolLanguage,
    LanguageToolMessage,
)


MESSAGE = Message(text="test", language="en-GB")


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

    lt_message = LanguageToolMessage(
        text="test", language="en-GB", motherTongue="en-GB"
    )
    map_message.return_value = lt_message

    url = backend.send_message_url

    reply = LanguageToolCorrectedMessage(
        language=LanguageToolLanguage(code="en-US"), matches=[]
    )
    post.return_value.json.return_value = reply

    corrected_message = CorrectedMessage(language="en-US", corrections=[])
    map_corrected_message.return_value = corrected_message

    result = backend.send_message(MESSAGE)

    map_message.assert_called_once_with(MESSAGE)
    post.assert_called_once_with(
        url, data=lt_message.dict(exclude_unset=True, exclude_none=True)
    )
    map_corrected_message.assert_called_once_with(reply)
    assert result == corrected_message


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


def test_parse_supported_languages(mocker, backend):
    Language = mocker.patch(
        "correction_adaptor.backends.languagetool.languagetool.Language"
    )
    language = Language(code="en-GB", name="British English")
    languagetool_language = {"name": "English (GB)", "code": "en", "longCode": "en-GB"}

    supported_languages = backend.parse_supported_languages([languagetool_language])
    assert supported_languages == [language]
