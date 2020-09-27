import responses

from starlette.testclient import TestClient

from main import app

client = TestClient(app)

SEND_MESSAGE_URL = "http://correction-backend-echo/message"


@responses.activate
def test_post_message():
    message = {"text": "hello"}
    reply = {"text": "hi"}

    responses.add(
        responses.POST,
        SEND_MESSAGE_URL,
        match=[responses.json_params_matcher(message)],
        json=reply,
        status=200,
    )

    response = client.post("/message", json=message)

    assert response.json() == reply
    assert response.status_code == 200


@responses.activate
def test_post_message_error():
    message = {"text": "hello"}

    responses.add(
        responses.POST,
        SEND_MESSAGE_URL,
        match=[responses.json_params_matcher(message)],
        status=500,
    )

    response = client.post("/message", json=message)
    assert response.status_code == 500
