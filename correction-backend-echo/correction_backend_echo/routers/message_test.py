from ..models import CorrectedMessage, Message
from .message import post, router


def test_router():
    assert len(router.routes) == 1
    route = router.routes[0]
    assert route.path == "/message"
    assert route.methods == {"POST"}


def test_post():
    text = "mock message"
    message = Message(text=text, language="no")
    reply = post(message)
    assert reply == CorrectedMessage(language="no", corrections=[])


def test_post_default_language():
    text = "mock message"
    message = Message(text=text)
    reply = post(message)
    assert reply == CorrectedMessage(language="en-US", corrections=[])
