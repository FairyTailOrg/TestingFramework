from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def find_element(self, selector: str):
        return self.page.locator(selector)

    def click(self, selector: str):
        self.page.locator(selector).click()

    def enter_text(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str):
        return self.page.locator(selector).inner_text()