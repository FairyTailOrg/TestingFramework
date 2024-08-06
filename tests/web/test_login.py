from tests.web.basetestcase import BaseTestCase

class TestLogin(BaseTestCase):

    def test_valid_login(self):
        self.navigate_to("https://example.com/login")
        self.fill_field("#username", "testuser")
        self.fill_field("#password", "testpass")
        self.click_button("#login")
        self.assert_text_in_element("body", "Welcome")

    def test_invalid_login(self):
        self.navigate_to("https://example.com/login")
        self.fill_field("#username", "wronguser")
        self.fill_field("#password", "wrongpass")
        self.click_button("#login")
        self.assert_text_in_element("body", "Invalid credentials")