from pydantic import BaseModel, BaseSettings, validator
from typing import Dict


class BackendSettings(BaseModel):
    base_url: str


class Settings(BaseSettings):
    backend: str
    backend_settings: Dict[str, BackendSettings]

    @validator("backend_settings")
    def backend_settings_must_contain_backend(
        cls, v: Dict[str, BackendSettings], values: dict
    ):
        backend = values["backend"]
        if backend not in v:
            raise ValueError(
                f"backend_settings does not contain an entry for the selected backend ({backend})"
            )
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
