from starlette.testclient import TestClient

from main import app

# client = TestClient(app)
# 
# 
# 
# def test_read_main():
    # response = client.get("/")
    # assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}
# 
# def test_post_message():
    # response = client.post("/message")
    # assert response.status_code == 200
    # response_obj = response.json()
    # assert 'text' in response_obj
