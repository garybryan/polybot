import responses

from starlette.testclient import TestClient

from correction_adaptor.main import app

client = TestClient(app)

SEND_MESSAGE_URL = "http://correction-backend-echo/message"


@responses.activate
def test_post_message():
    message = {"text": "hello"}
    reply = {"text": "hi"}

    from correction_adaptor.settings import Settings

    # TODO handle errors and test it
    responses.add(responses.POST, SEND_MESSAGE_URL, json=reply, status=200)

    response = client.post("/message", json=message)

    assert response.json() == reply
    assert response.status_code == 200
