"""This file will contain all the web libraries used for project."""
import os

from playwright.sync_api import Page

from lib.logger_config import setup_logger
from pages.pom import Pom


class LoginPage:
    """This class will contain all the types of login."""

    def __init__(self, page: Page):
        """Initialize the playwright functions.

        Args:
            page (Page): page playwright function.
        """
        self.page = page
        self.pom = Pom()
        self.logger = setup_logger()

    def go_to_landing_page(self, login_url: str):
        """Receives the url and go to it.

        Args:
            login_url (str): url to be redirected.
        """
        self.page.goto(login_url)
        self.page.wait_for_selector(self.pom.landingpage.lodus_icon_desktop)

    def login_existent_patient(self, username: str, password: str):
        """Login as an existent patient flow.

        Args:
            username (str): user creds.
            password (str): password creds.

        Returns:
            boolean: True if login was succesful.
        """
        url = os.getenv("FRONTEND_URL")  # Get the url used.
        self.go_to_landing_page(url)
        self.page.click(self.pom.landingpage.login_button_desktop)
        try:
            self.page.click(self.pom.login_modal.accept_terms_of_use)
        except Exception as e:
            self.logger.error(f"Error al aceptar los términos de uso: {e}")
        self.page.click(self.pom.login_modal.login_button)

        self.page.wait_for_selector(self.pom.athena_cred.email_input)
        self.page.fill(self.pom.athena_cred.email_input, username)
        self.page.fill(self.pom.athena_cred.password_input, password)
        self.page.click(self.pom.athena_cred.login_button)
        self.page.click(self.pom.athena_cred.select_department)

        self.page.wait_for_url(f"{url}/dashboard")
        return True
