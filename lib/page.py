class Page:
    def __init__(self, context):
        self.page = context.new_page()

    def navigate(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def close(self):
        self.page.close()
