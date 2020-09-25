from ..models import Message
from ..settings import BackendSettings
from .languagetool import LanguageToolBackend

URL = "http://backend-languagetool/"


def test_send_message(mocker):
    post = mocker.patch("requests.post")

    backend = LanguageToolBackend(BackendSettings(base_url=URL))
    message = Message(text="test")
    url = backend.send_message_url

    reply = Message(text="reply")
    post.return_value.json.return_value = reply

    result = backend.send_message(message)

    post.assert_called_once_with(url, json=message.dict())
    assert result == reply
