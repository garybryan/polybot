import unittest
from unittest.mock import patch

from main import post_message


class TestMessage(unittest.TestCase):
    @patch("main.post", return_value="mock response")
    def test_post(self, backend):
        message = "mock message"
        result = post_message(message)
        self.assertEqual(result, "mock response")
