import pytest

class BaseTestCase:
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page

    def navigate_to(self, url):
        self.page.goto(url)

    def fill_field(self, selector, value):
        self.page.fill(selector, value)

    def click_button(self, selector):
        self.page.click(selector)

    def assert_text_in_element(self, selector, expected_text):
        actual_text = self.page.text_content(selector)
        assert expected_text in actual_text, f"Expected '{expected_text}' to be in '{actual_text}'"