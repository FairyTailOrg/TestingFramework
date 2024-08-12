# pages/login_page.py

from playwright.sync_api import Page
from selenium.webdriver.common.by import By

from .base_page import BasePage


class LandingPage:
    def __init__(self):
        self.lodus_icon_mobile = '(//header//div/a//img)[1]'
        self.lodus_icon_desktop = '(//header//div/a//img)[2]'
        self.login_button_mobile = '(//*[@id="login_button"])[1]'
        self.login_button_desktop = '(//*[@id="login_button"])[2]'

class LoginModal:
    def __init__(self):
        self.accept_terms_of_use = "//div/span/input"
        self.login_button = "//div/button[contains(text(), 'Log in with')]"
        self.create_account_button = '/html/body//div/a[contains(text(), "Create Account")]'

class AthenaCred:
    def __init__(self):
        self.email_input = "//div/span/input[@id='okta-signin-username']"
        self.password_input = "//div/span/input[@id='okta-signin-password']"
        self.login_button = "//div/input[@id='okta-signin-submit']"
        self.select_department = "//div[@class='patient-record-item picker']"
