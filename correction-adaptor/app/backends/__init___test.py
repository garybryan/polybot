from ..test.helpers import MockBackend, mock_backend_with_settings


def test_backend(mocker):
    mocker.patch("app.backends.backend", mock_backend_with_settings())
    from . import backend

    assert isinstance(backend, MockBackend)
