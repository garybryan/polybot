import responses

from starlette.testclient import TestClient

from main import app

client = TestClient(app)

SEND_MESSAGE_URL = "http://correction-backend-echo/message"
MESSAGE = {"text": "hello", "language": "en-GB", "user_language": None}


@responses.activate
def test_post_message():
    reply = {"text": "hello", "language": "en-GB", "corrections": []}

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


def test_post_message_missing():
    response = client.post("/message", json={})

    assert response.status_code == 422


@responses.activate
def test_post_message_error():

    responses.add(
        responses.POST,
        SEND_MESSAGE_URL,
        match=[responses.json_params_matcher(MESSAGE)],
        status=500,
    )

    response = client.post("/message", json=MESSAGE)
    assert response.status_code == 500


def test_get_message_not_allowed():
    response = client.get("/message", json=MESSAGE)
    assert response.status_code == 405
