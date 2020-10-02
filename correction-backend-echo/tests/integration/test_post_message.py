from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_post_message():
    message = {"text": "hello!"}
    reply = {"text": "You said: hello!", "language": "en-GB"}

    response = client.post("/message", json=message)

    assert response.json() == reply
    assert response.status_code == 200


def test_get_message_not_allowed():
    message = {"text": "hello"}
    response = client.get("/message", json=message)
    assert response.status_code == 405
