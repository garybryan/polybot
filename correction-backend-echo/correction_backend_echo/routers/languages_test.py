from correction_adaptor.models import Language
from .languages import get, router


def test_router():
    assert len(router.routes) == 1
    route = router.routes[0]
    assert route.path == "/languages"
    assert route.methods == {"GET"}


def test_get():
    result = get()
    assert result == [Language(name="English (British)", code="en-GB")]