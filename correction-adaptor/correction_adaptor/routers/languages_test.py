from unittest.mock import PropertyMock
from ..test.helpers import mock_backend_with_settings
from .languages import get, router


def test_router():
    assert len(router.routes) == 1
    route = router.routes[0]
    assert route.path == "/languages"
    assert route.methods == {"GET"}


def test_get(mocker):
    supported_languages = mocker.patch(
        "correction_adaptor.test.helpers.MockBackend.supported_languages",
        new_callable=PropertyMock,
    )
    mocker.patch(
        "correction_adaptor.routers.languages.get_backend",
        return_value=mock_backend_with_settings(),
    )

    get()
    supported_languages.assert_called_once_with()
