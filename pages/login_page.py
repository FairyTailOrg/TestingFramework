# pages/login_page.py

from playwright.sync_api import Page
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LandingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.lodus_icon_mobile = (By.XPATH, ('//*[@id="__next"]/header/div//div/a/img')[0])
        self.lodus_icon_desktop = (By.XPATH, ('//*[@id="__next"]/header/div//div/a/img')[1])
        self.login_button_mobile = (By.XPATH, ('//*[@id="login_button"]')[0])
        self.login_button_desktop = (By.XPATH, ('//*[@id="login_button"]')[1])

class LoginModal(LandingPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_button = "//div/button[contains(text(), 'Log in with')]"
        self.create_account_button = '/html/body//div/a[contains(text(), "Create Account")]'

class AthenaCreds:
        def __init__(self):
            self.email_input = (By.XPATH, '//div')
            self.password_input = (By.XPATH, '//input[@name="password"]')


    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)