import unittest
from unittest.mock import patch

from message.post import post


class TestMessage(unittest.TestCase):
    @patch('message.post.backend')
    def test_post(self, backend):
        message = 'mock message'
        post(message)
        backend.send_message.assert_called_once_with(message)
