"""This file will contain all the pom to try to login."""


class LoginModal:
    """Login page class to navigate in page."""

    def __init__(self):
        """Get all the xpath locators for login modal."""
        self.modal_inputs = "//*[@id='loginform']"
        self.username = self.modal_inputs + "//div/input[@name='username']"
        self.password = self.modal_inputs + "//div/input[@name='password']"
        self.login_button = self.modal_inputs + "//div/input[@value='Log In']"
        self.loading_icon = "//div[@class='overlay__loading']"
