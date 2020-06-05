from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_post_message():
    sent_text = 'Test text'
    response = client.post("/message", json={
        'text': sent_text
    })
    print(response)
    assert response.status_code == 200
    response_obj = response.json()
    assert 'text' in response_obj
    assert response_obj['text'] == sent_text
