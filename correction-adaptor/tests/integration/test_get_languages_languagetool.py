import json
import os
import pytest
import responses

from pytest_mock.plugin import MockerFixture
from requests.exceptions import ConnectionError
from starlette.testclient import TestClient

from main import app

FIXTURE_BASE = "tests/fixtures/"
RESPONSE_FIXTURE_BASE = f"{FIXTURE_BASE}responses/"
PROVIDER_FIXTURE_BASE = f"{FIXTURE_BASE}providers/languagetool/"


BACKEND = "languagetool"
BASE_URL = "http://languagetool/api"
BACKEND_SETTINGS = {"languagetool": {"base_url": BASE_URL}}
MOCK_ENV = {"backend": BACKEND, "backend_settings": json.dumps(BACKEND_SETTINGS)}

SUPPORTED_LANGUAGES_URL = f"{BASE_URL}/languages"


@pytest.fixture
def client(mocker: MockerFixture):
    mocker.patch.dict(os.environ, MOCK_ENV)
    return TestClient(app)


@responses.activate
def test_get_supported_languages(client: TestClient):
    with open(f"{PROVIDER_FIXTURE_BASE}response.languages.json") as f:
        provider_reply = json.load(f)

    with open(f"{RESPONSE_FIXTURE_BASE}response.languages.json") as f:
        expected_reply = json.load(f)

    responses.add(
        responses.GET,
        SUPPORTED_LANGUAGES_URL,
        json=provider_reply,
        status=200,
    )

    response = client.get("/languages")

    assert response.json() == expected_reply
    assert response.status_code == 200


@responses.activate
def test_get_supported_languages_empty(client: TestClient):
    provider_reply = []
    expected_reply = []

    responses.add(
        responses.GET,
        SUPPORTED_LANGUAGES_URL,
        json=provider_reply,
        status=200,
    )

    response = client.get("/languages")

    assert response.json() == expected_reply
    assert response.status_code == 200


@responses.activate
def test_get_supported_languages_error(client: TestClient):
    responses.add(
        responses.GET, SUPPORTED_LANGUAGES_URL, status=403, body="Permission denied"
    )

    response = client.get("/languages")
    assert response.status_code == 403
    assert response.json() == {"message": "Permission denied"}


@responses.activate
def test_get_supported_languages_connection_error(client: TestClient):

    responses.add(
        responses.GET, SUPPORTED_LANGUAGES_URL, body=ConnectionError("Cannot connect")
    )

    response = client.get("/languages")
    assert response.status_code == 502
    assert response.json() == {"message": "Cannot connect"}


def test_get_message_not_allowed(client: TestClient):
    response = client.post("/languages")
    assert response.status_code == 405
