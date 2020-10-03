import os
import pytest
import json
import responses

from pytest_mock.plugin import MockerFixture
from starlette.testclient import TestClient

from main import app

BACKEND = "echo"
BASE_URL = "http://correction-backend-echo"
BACKEND_SETTINGS = {"echo": {"base_url": BASE_URL}}
MOCK_ENV = {"backend": BACKEND, "backend_settings": json.dumps(BACKEND_SETTINGS)}

SEND_MESSAGE_URL = f"{BASE_URL}/message"
MESSAGE = {"text": "hello", "language": "en-GB"}


@pytest.fixture
def client(mocker: MockerFixture):
    mocker.patch.dict(os.environ, MOCK_ENV)
    return TestClient(app)


@responses.activate
def test_post_message(client: TestClient):
    reply = {"language": "en-GB", "corrections": []}

    responses.add(
        responses.POST,
        SEND_MESSAGE_URL,
        match=[responses.json_params_matcher(MESSAGE)],
        json=reply,
        status=200,
    )

    response = client.post("/message", json=MESSAGE)

    assert response.json() == reply
    assert response.status_code == 200


def test_post_message_missing(client: TestClient):
    response = client.post("/message", json={})

    assert response.status_code == 422


@responses.activate
def test_post_message_error(client: TestClient):

    responses.add(
        responses.POST,
        SEND_MESSAGE_URL,
        match=[responses.json_params_matcher(MESSAGE)],
        status=500,
    )

    response = client.post("/message", json=MESSAGE)
    assert response.status_code == 500


def test_get_message_not_allowed(client: TestClient):
    response = client.get("/message", json=MESSAGE)
    assert response.status_code == 405
