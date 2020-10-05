from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_languages():
    reply = [{"name": "English (British)", "code": "en-GB"}]

    response = client.get("/languages")

    assert response.json() == reply
    assert response.status_code == 200
