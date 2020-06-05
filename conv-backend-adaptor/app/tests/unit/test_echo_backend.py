import unittest
from unittest.mock import Mock, patch

from backends.echo import EchoBackend
from config import BACKEND_ECHO
from models import Message


class TestMessage(unittest.TestCase):
    # TODO common base class
    def __init__(self, *args, **kwargs):
        self.backend = EchoBackend()
        super().__init__(*args, **kwargs)

    @patch('requests.post')
    def test_send_message(self, post):
        message = Message(text='test')
        url = EchoBackend.SEND_MESSAGE_URL

        reply = Message(text='reply')
        post.return_value.json.return_value = reply

        result = self.backend.send_message(message)

        post.assert_called_once_with(url, json=message.dict())
        self.assertEqual(result, reply)
