from ..settings import Settings
from .echo import EchoBackend
from .languagetool import LanguageToolBackend


BACKENDS = {
    "echo": EchoBackend,
    "languagetool": LanguageToolBackend,
}


def get_backend():
    settings = Settings()
    return BACKENDS[settings.backend](settings.backend_settings[settings.backend])


backend = get_backend()
