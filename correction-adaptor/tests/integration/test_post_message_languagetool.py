import json
import os
import pytest
import responses

from pytest_mock.plugin import MockerFixture

from starlette.testclient import TestClient
from main import app

FIXTURE_BASE = "tests/fixtures/"
RESPONSE_FIXTURE_BASE = f"{FIXTURE_BASE}responses/"
PROVIDER_FIXTURE_BASE = f"{FIXTURE_BASE}providers/languagetool/"


BACKEND = "languagetool"
BASE_URL = "http://languagetool/api"
BACKEND_SETTINGS = {"languagetool": {"base_url": BASE_URL}}
MOCK_ENV = {"backend": BACKEND, "backend_settings": json.dumps(BACKEND_SETTINGS)}

SEND_MESSAGE_URL = f"{BASE_URL}/check"


@pytest.fixture
def client(mocker: MockerFixture):
    mocker.patch.dict(os.environ, MOCK_ENV)
    return TestClient(app)


@responses.activate
def test_post_message(client: TestClient):
    message = {"text": "hello", "language": "en-GB", "user_language": None}
    lt_message = {"text": "hello", "language": "en-GB"}

    with open(f"{PROVIDER_FIXTURE_BASE}response.success.no-corrections.json") as f:
        provider_reply = json.load(f)

    with open(f"{RESPONSE_FIXTURE_BASE}response.success.no-corrections.json") as f:
        expected_reply = json.load(f)

    responses.add(
        responses.POST,
        SEND_MESSAGE_URL,
        match=[responses.json_params_matcher(lt_message)],
        json=provider_reply,
        status=200,
    )

    response = client.post("/message", json=message)

    assert response.json() == expected_reply
    assert response.status_code == 200


@responses.activate
def test_post_message_corrections(client: TestClient):
    message = {
        "text": "I went their yestreday",
        "language": "en-GB",
        "user_language": "fr-FR",
    }
    lt_message = {
        "text": "I went their yestreday",
        "language": "en-GB",
        "motherTongue": "fr-FR",
    }

    with open(f"{PROVIDER_FIXTURE_BASE}response.success.corrections.json") as f:
        provider_reply = json.load(f)

    with open(f"{RESPONSE_FIXTURE_BASE}response.success.corrections.json") as f:
        expected_reply = json.load(f)

    responses.add(
        responses.POST,
        SEND_MESSAGE_URL,
        match=[responses.json_params_matcher(lt_message)],
        json=provider_reply,
        status=200,
    )

    response = client.post("/message", json=message)

    assert response.json() == expected_reply
    assert response.status_code == 200


def test_post_message_missing(client: TestClient):
    message = {}

    response = client.post("/message", json=message)

    assert response.status_code == 422


@responses.activate
def test_post_message_error(client: TestClient):
    message = {"text": "hello", "language": "en-GB"}

    responses.add(
        responses.POST,
        SEND_MESSAGE_URL,
        match=[responses.json_params_matcher(message)],
        status=500,
    )

    response = client.post("/message", json=message)
    assert response.status_code == 500


def test_get_message_not_allowed(client: TestClient):
    message = {"text": "hello"}
    response = client.get("/message", json=message)
    assert response.status_code == 405
