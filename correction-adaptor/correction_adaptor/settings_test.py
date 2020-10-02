import json
import os
import pytest

from pydantic.error_wrappers import ValidationError

from .settings import Settings

BACKEND = "mock_backend"
BASE_URL = "http://mock-backend"
BACKEND_SETTINGS = {"mock_backend": {"base_url": BASE_URL}}
MOCK_ENV = {"backend": BACKEND, "backend_settings": json.dumps(BACKEND_SETTINGS)}


@pytest.fixture
def mock_env(mocker):
    mocker.patch.dict(os.environ, MOCK_ENV)


def test_settings_env(mock_env):
    settings_dict = Settings().dict()
    assert settings_dict["backend"] == BACKEND
    assert settings_dict["backend_settings"]["mock_backend"]["base_url"] == BASE_URL


def test_settings_merge(mock_env):
    new_backend = "new_backend"
    new_url = "http://new-backend/api"
    settings_dict = Settings(
        backend=new_backend, backend_settings={"new_backend": {"base_url": new_url}}
    ).dict()
    assert settings_dict["backend"] == new_backend
    assert settings_dict["backend_settings"]["mock_backend"]["base_url"] == BASE_URL
    assert settings_dict["backend_settings"]["new_backend"]["base_url"] == new_url


def test_backend_settings_must_contain_backend(mock_env):
    new_backend = "new_backend"
    with pytest.raises(ValidationError) as exc_info:
        Settings(backend=new_backend)
    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert (
        errors[0]["msg"]
        == f"backend_settings does not contain an entry for the selected backend ({new_backend})"
    )
