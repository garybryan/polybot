from .chatterbot import ChatterbotBackend
from .echo import EchoBackend

import config

BACKENDS = {
    "chatterbot": ChatterbotBackend,
    "echo": EchoBackend,
}

backend = BACKENDS[config.BACKEND]()
