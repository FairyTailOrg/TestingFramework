"""File with all the home page elements."""
from playwright.sync_api import Page


class HomePage:
    """Home page class to navigate in page."""

    def __init__(self):
        """Get all the xpath locators for home page."""
        self.logo_desktop = "(//div/a[@href='https://www.akc.org'])[1]"
        self.nav_bar = "//div//nav[@class='utility-nav']"
        self.event = self.nav_bar + "/a[contains(., 'Event Search')]"
        self.f_puppy = self.nav_bar + "/a[contains(., 'Find a Puppy')]"
        self.register = self.nav_bar + "/a[contains(., 'Register')]"
        self.shop = self.nav_bar + "/a[contains(., 'Shop')]"
        self.tv = self.nav_bar + "/a[contains(., 'AKC TV')]"
        self.rx = self.nav_bar + "/a[contains(., 'AKC Rx')]"
        self.sign_in = "//div//nav[@class='utility-nav sign-in-nav']/a"
        self.search = "//div//input[@id='desktop-search']"
        self.prim_nav = "//div/nav[@class='primary-nav__group']"
        self.breed = self.prim_nav + "/a[contains(., 'BREEDS A-Z')]"
        self.advice = self.prim_nav + "/a[contains(., 'EXPERT ADVICE')]"
        self.service = self.prim_nav + "/a[contains(., 'PRODUCTS & SERVICES')]"
        self.sports = self.prim_nav + "/a[contains(., 'SPORTS & EVENTS')]"
        self.club = self.prim_nav + "/a[contains(., 'CLUB & DELEGATES')]"
        self.search_breed = "//*[@id='homepage-hero-breed-search-selectized']"
        self.logo_mobile = "(//div/a[@href='https://www.akc.org'])[2]"


class LoginModal:
    """Login modal class to navigate in page."""

    def __init__(self):
        """Get all the xpath locators for login modal."""
        self.modal_inputs = "//*[@id='gigya-login-form']"
        self.username = self.modal_inputs + "//div/input[@name='username']"
        self.password = self.modal_inputs + "//div/input[@name='password']"
        self.login_button = self.modal_inputs + "//div/input[@value='Log In']"
        self.loading_icon = "//div[@class='overlay__loading']"
