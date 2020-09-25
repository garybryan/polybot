from functools import partial

from ..settings import Settings
from ..test.helpers import MockBackend
from .base import Backend

BASE_URL = "http://mock-backend"

patch_settings = partial(
    Settings,
    backend="mock_backend",
    backend_settings={"mock_backend": {"base_url": "http://mock-backend"}},
)


def test_backends_subclass_backend():
    from .backends import BACKENDS

    for backend in BACKENDS.values():
        assert issubclass(backend, Backend)


def test_get_backend(mocker):
    mocker.patch.dict(
        "correction_adaptor.backends.backends.BACKENDS", {"mock_backend": MockBackend}
    )
    mocker.patch("correction_adaptor.backends.backends.Settings", patch_settings)
    from .backends import get_backend

    backend = get_backend()
    assert isinstance(backend, MockBackend)
