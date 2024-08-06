import os
from dotenv import load_dotenv
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def browser(playwright, request):
    browser = getattr(playwright, request.param).launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")

@pytest.fixture(scope="session", autouse=True)
def load_env():
    environment = os.getenv("ENV", "development")
    if environment == "production":
        load_dotenv("config/config_production.env")
    elif environment == "qa":
        load_dotenv("config/config_qa.env")
    else:
        load_dotenv("config/config_dev.env")