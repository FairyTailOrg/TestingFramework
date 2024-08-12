from tests.web.basetestcase import BaseTestCase


class TestLogin(BaseTestCase):
    def test_valid_login(self):
        self.navigate_to("https://example.com/login")
