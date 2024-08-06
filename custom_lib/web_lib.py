from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_login_page(self, login_url: str):
        """Navega a la página de inicio de sesión."""
        self.page.goto(login_url)

    def login(self, username: str, password: str, username_selector: str, password_selector: str, submit_button_selector: str):
        """Realiza el login con las credenciales proporcionadas."""
        self.page.fill(username_selector, username)
        self.page.fill(password_selector, password)
        self.page.click(submit_button_selector)
        self.page.wait_for_navigation()

    def login_and_verify(self, login_url: str, username: str, password: str, username_selector: str, password_selector: str, submit_button_selector: str):
        """Realiza el login y verifica el éxito."""
        self.navigate_to_login_page(login_url)
        self.login(username, password, username_selector, password_selector, submit_button_selector)

        # Verifica si el login fue exitoso
        return self.page.url != login_url