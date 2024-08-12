# pages/login_page.py

from playwright.sync_api import Page
from selenium.webdriver.common.by import By

from .base_page import BasePage


class LandingPage:
    def __init__(self):
        self.lodus_icon_mobile = (By.XPATH, ('//*[@id="__next"]/header/div//div/a/img')[0])
        self.lodus_icon_desktop = (By.XPATH, ('//*[@id="__next"]/header/div//div/a/img')[1])
        self.login_button_mobile = (By.XPATH, ('//*[@id="login_button"]')[0])
        self.login_button_desktop = (By.XPATH, ('//*[@id="login_button"]')[1])

class LoginModal:
    def __init__(self):
        self.accept_terms_of_use = "/html/body//div/span/input"
        self.login_button = "//div/button[contains(text(), 'Log in with')]"
        self.create_account_button = '/html/body//div/a[contains(text(), "Create Account")]'

class AthenaCred:
    def __init__(self):
        self.email_input = (By.XPATH, "//div/span/input[@id='okta-signin-username']")
        self.password_input = (By.XPATH, "//div/span/input[@id='okta-signin-password']")
        self.login_button = (By.XPATH, "//div/input[@id='okta-signin-submit']")
        self.select_department = (By.XPATH, "//div[@class='patient-record-item picker']")
