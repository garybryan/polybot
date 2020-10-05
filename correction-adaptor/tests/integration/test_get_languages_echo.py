import json
import os
import pytest
import responses

from requests.exceptions import ConnectionError
from pytest_mock.plugin import MockerFixture
from starlette.testclient import TestClient

from main import app

BACKEND = "echo"
BASE_URL = "http://correction-backend-echo"
BACKEND_SETTINGS = {"echo": {"base_url": BASE_URL}}
MOCK_ENV = {"backend": BACKEND, "backend_settings": json.dumps(BACKEND_SETTINGS)}

SUPPORTED_LANGUAGES_URL = f"{BASE_URL}/languages"


@pytest.fixture
def client(mocker: MockerFixture):
    mocker.patch.dict(os.environ, MOCK_ENV)
    return TestClient(app)


@responses.activate
def test_get_supported_languages(client: TestClient):
    reply = [{"name": "English", "code": "en"}, {"name": "French", "code": "fr"}]

    responses.add(
        responses.GET,
        SUPPORTED_LANGUAGES_URL,
        json=reply,
        status=200,
    )

    response = client.get("/languages")

    assert response.json() == reply
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
