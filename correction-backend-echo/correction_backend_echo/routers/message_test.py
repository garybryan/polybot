from ..models import Message
from .message import post, router


def test_router():
    assert len(router.routes) == 1
    route = router.routes[0]
    assert route.path == "/message"
    assert route.methods == {"POST"}


def test_post():
    text = "mock message"
    message = Message(text=text, language="en-GB")
    reply = post(message)
    assert reply.text == f"You said: {text}"
    assert reply.language == "en-GB"
