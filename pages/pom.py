"""This module will contain all the schemas instanced."""
from pages.home_page import HomePage, LoginModal


class Pom:
    """Class to instance all the schemas."""

    def __init__(self):
        """Initialize all the clases which convert the json to dict."""
        self.home = HomePage()
        self.login_modal = LoginModal()
