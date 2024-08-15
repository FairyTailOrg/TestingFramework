"""This module will contain all the schemas instanced."""
from pages.login_page import AthenaCred, LandingPage, LoginModal


class Pom:
    """Class to instance all the schemas."""

    def __init__(self):
        """Initialize all the clases which convert the json to dict."""
        self.landingpage = LandingPage()
        self.login_modal = LoginModal()
        self.athena_cred = AthenaCred()
