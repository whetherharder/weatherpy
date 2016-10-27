from unittest import TestCase
from ..client import Client


class TestClient(TestCase):
    user, password = '', ''
    client = None

    def setUp(self):
        self.client = Client()

    def test_login(self):
        is_logged = self.client.login(user=self.user, password=self.password)
        self.assertTrue(is_logged)

    def test_session_not_not_null(self):
        session = self.client.get_session()
        self.assertIsNotNone(session)
