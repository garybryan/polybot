import unittest
import responses
import requests

from starlette.testclient import TestClient

from backends import backend
from main import app
from models import Message

client = TestClient(app)


class TestApp(unittest.TestCase):
    @responses.activate
    def test_post_message(self):
        message = Message(text='hello')
        reply = Message(text='hi')

        # TODO support testing multiple backends
        # TODO handle errors and test it
        responses.add(responses.POST, backend.SEND_MESSAGE_URL, json=reply.dict(), status=200)

        response = client.post("/message", json=message.dict())

        self.assertEqual(response.json(), reply.dict())
        self.assertEqual(response.status_code, 200)

