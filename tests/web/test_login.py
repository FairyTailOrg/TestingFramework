import os

from tests.web.basetestcase import BaseTestCase


class TestLogin(BaseTestCase):
    def test_valid_login(self):
        username = os.getenv("EXISTENTPATIENT_USER")
        password = os.getenv("EXISTENTPATIENT_PASSWORD")
        self.login.login(username, password)