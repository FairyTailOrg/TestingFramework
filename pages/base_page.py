"""File with all the base_page options."""
from playwright.sync_api import Page


class BasePage:
    """Base page class to start with playwright."""

    def __init__(self, page: Page):
        """Initialize of page class.

        Args:
            page (Page): Page playwright class.
        """
        self.page = page

    def goto(self, url: str):
        """Go to specified url.

        Args:
            url (str): url to be redirected.
        """
        self.page.goto(url)

    def find_element(self, selector: str):
        """Find element.

        Args:
            selector (str): selector to be found.

        Returns:
            _type_: selector found object.
        """
        return self.page.locator(selector)

    def click(self, selector: str):
        """Click on the element.

        Args:
            selector (str): element to be clicked.
        """
        self.page.locator(selector).click()

    def enter_text(self, selector: str, text: str):
        """Text to be inserted.

        Args:
            selector (str): Selector which receives the text.
            text (str): Text to be introduced in the selector.
        """
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str):
        """Get specific text from a element.

        Args:
            selector (str): selector which a text.

        Returns:
            _type_: Text of the element.
        """
        return self.page.locator(selector).inner_text()
