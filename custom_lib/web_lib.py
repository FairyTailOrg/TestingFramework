import os

from playwright.sync_api import Page

from lib.logger_config import setup_logger
from pages.pom import Pom


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.pom = Pom()
        self.logger = setup_logger()
        
    def go_to_landing_page(self, login_url: str):
        """Navega a la página de inicio de sesión."""
        self.page.goto(login_url)
        self.page.wait_for_selector(self.pom.landingpage.lodus_icon_desktop)

    def login(self, username: str, password: str):
        """Realiza el login con las credenciales proporcionadas."""
        url = os.getenv("FRONTEND_URL")  # Get the url used.
        self.logger.info(url)
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

        if self.page.wait_for_url == "{url}/dashboard":
            return True
        return False





