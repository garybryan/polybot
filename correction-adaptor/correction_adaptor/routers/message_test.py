from ..models import Message
from ..test.helpers import mock_backend_with_settings
from .message import post, router


def test_router():
    assert len(router.routes) == 1
    route = router.routes[0]
    assert route.path == "/message"
    assert route.methods == {"POST"}


def test_post(mocker):
    send_message = mocker.patch(
        "correction_adaptor.test.helpers.MockBackend.send_message"
    )
    mocker.patch(
        "correction_adaptor.routers.message.get_backend",
        return_value=mock_backend_with_settings(),
    )

    message = Message(text="mock message")
    post(message)
    send_message.assert_called_once_with(message)
