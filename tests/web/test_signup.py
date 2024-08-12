from tests.web.basetestcase import BaseTestCase

class TestSignup(BaseTestCase):
    def test_valid_signup(page):
        page.goto("https://example.com/signup")
        page.fill("#username", "newuser")
        page.fill("#email", "newuser@example.com")
        page.fill("#password", "newpass")
        page.click("#signup")
        assert "Thank you for signing up!" in page.text_content("body")