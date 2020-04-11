from .chatterbot import ChatterbotBackend

import config

BACKENDS = {
    'chatterbot': ChatterbotBackend
}

backend = BACKENDS[config.BACKEND]()
