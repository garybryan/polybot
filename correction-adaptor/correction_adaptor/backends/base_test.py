import pytest

from requests.exceptions import ConnectionError, HTTPError

from ..settings import BackendSettings
from ..test.helpers import MockBackend

BASE_URL = "http://mock-backend"
SEND_MESSAGE_PATH = "/message"
SUPPORTED_LANGUAGES_PATH = "/languages"


SETTINGS = BackendSettings(base_url=BASE_URL)


@pytest.fixture
def backend() -> MockBackend:
    return MockBackend(SETTINGS)


def test_base(backend: MockBackend):
    assert backend.send_message_url == f"{BASE_URL}{SEND_MESSAGE_PATH}"
    assert backend.supported_languages_url == f"{BASE_URL}{SUPPORTED_LANGUAGES_PATH}"


def test_parse_supported_languages(mocker, backend: MockBackend):
    Language = mocker.patch("correction_adaptor.backends.base.Language")
    language = Language(code="en-GB", name="British English")
    language_dict = {"test": "language"}
    Language.parse_obj.return_value = language

    result = backend.parse_supported_languages([language_dict])

    Language.parse_obj.assert_called_once_with(language_dict)
    assert result == [language]


def test_get_supported_languages(mocker, backend: MockBackend):
    Language = mocker.patch("correction_adaptor.backends.base.Language")
    language = Language(code="en-GB", name="British English")
    language_dict = {"test": "language"}

    parse_supported_languages = mocker.patch.object(
        backend, "parse_supported_languages"
    )
    parse_supported_languages.return_value = [language]

    get = mocker.patch("requests.get")
    get.return_value.json.return_value = [language_dict]
    url = backend.supported_languages_url

    result = backend.get_supported_languages()

    parse_supported_languages.assert_called_once_with([language_dict])
    get.assert_called_once_with(url)
    assert result == [language]


def test_send_message_connection_error(mocker, backend):
    get = mocker.patch("requests.get")

    get.side_effect = ConnectionError()

    with pytest.raises(ConnectionError):
        backend.get_supported_languages()


def test_send_message_http_error(mocker, backend):
    get = mocker.patch("requests.get")
    get.return_value.raise_for_status.side_effect = HTTPError()

    with pytest.raises(HTTPError):
        backend.get_supported_languages()
