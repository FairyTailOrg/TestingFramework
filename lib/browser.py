from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self, browser_type='chromium'):
        self.browser_type = browser_type
        self.browser = None
        self.context = None

    def launch(self):
        with sync_playwright() as p:
            if self.browser_type == 'firefox':
                self.browser = p.firefox.launch()
            elif self.browser_type == 'webkit':
                self.browser = p.webkit.launch()
            else:
                self.browser = p.chromium.launch()
            self.context = self.browser.new_context()
            return self.context

    def close(self):
        if self.browser:
            self.browser.close()