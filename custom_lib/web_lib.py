"""This file will contain all the web libraries used for project."""
import os
import re

from playwright.sync_api import Page

from lib.logger_config import logger
from pages.pom import Pom


class HomePage:
    """This class will contain all the types of login."""

    def __init__(self, page: Page):
        """Initialize the playwright functions.

        Args:
            page (Page): page playwright function.
        """
        self.page = page
        self.pom = Pom()
        self.logger = logger
        self.url = os.getenv("FRONTEND_URL")

    def go_to_home_page(self, login_url: str):
        """Receives the url and go to it.

        Args:
            login_url (str): url to be redirected.
        """
        self.page.goto(login_url)
        self.page.wait_for_selector(self.pom.home.logo_desktop)

    def login(self, username: str, password: str):
        """Login as an existent patient flow.

        Args:
            username (str): user creds.
            password (str): password creds.

        Returns:
            boolean: True if login was succesful.
        """
        self.go_to_home_page(self.url)

        user_button = self.page.locator(self.pom.home.sign_in)
        if "Sign In" not in user_button.text_content():
            raise ValueError("Not available to login.")
        user_button.click()

        self.page.fill(self.pom.login_modal.username, username)
        self.page.fill(self.pom.login_modal.password, password)

        self.page.click(self.pom.login_modal.login_button)

        self.page.wait_for_selector(
            self.pom.login_modal.login_button,
            state="detached"
            )
        self.page.wait_for_selector(self.pom.login_modal.loading_icon)
        self.page.wait_for_selector(
            self.pom.login_modal.loading_icon,
            state="detached"
            )
        self.page.wait_for_url(f"{self.url}")
        final_user = self.page.locator(self.pom.home.sign_in)
        show_user = final_user.text_content()
        if "Sign In" in show_user:
            return False
        show_user = show_user.replace("\n", "")
        show_user = show_user.replace("\t", "")
        show_user = show_user.replace(" ", "")
        show_user = re.sub(r'([a-z])([A-Z])', r'\1 \2', show_user)
        self.logger.info(f"User logged: {show_user}")
        return True

    def check_utility_headers(self):
        """Check if utility headers are available."""
        self.go_to_home_page(self.url)
        headers = self.page.locator(self.pom.home.nav_bar+"/a")
        return headers.all_inner_texts()
