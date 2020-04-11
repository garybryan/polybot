import unittest

import config
from backends import BACKENDS, backend
from backends.base import Backend


class TestMessage(unittest.TestCase):
    def test_backends_subclass_backend(self):
        map(lambda be: self.assertIsInstance(be, Backend), BACKENDS.values())

    def test_configured_backend_in_backends(self):
        self.assertIn(config.BACKEND, BACKENDS)