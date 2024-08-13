import datetime
import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from custom_lib.web_lib import LoginPage
from lib.logger_config import setup_logger


@pytest.fixture(scope="session")
def logger():
    return setup_logger()

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    browser_option = pytestconfig.getoption("browser").lower()
    if browser_option == "all":
        return ["chromium", "firefox", "webkit"]
    elif browser_option in ["chromium", "firefox", "webkit"]:
        return [browser_option]
    else:
        raise ValueError(f"Unsupported browser option: {browser_option}")
    
@pytest.fixture(scope="session")
def browsers(pytestconfig, playwright, browser_name):
    return [getattr(playwright, name).launch(headless=pytestconfig.getoption("headless")) for name in browser_name]

@pytest.fixture(scope="function")
def browser(browsers, request):
    return browsers[request.param] if hasattr(request, 'param') else browsers[0]

@pytest.hookimpl(tryfirst=True)
def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames and metafunc.config.getoption("browser") == "all":
        metafunc.parametrize("browser", range(len(metafunc.config._metadata["browsers"])))

@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()
    yield page

    page.close()
    context.close()

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Environment to run tests against")
    parser.addoption("--browser", action="store", default="chromium", help="Browser to execute the test, you can use: chromium, firefox, webkit or All(for the 3 mentioned before)")
    parser.addoption("--headless", action="store_true", default=False, help="Choose if headless or not")

@pytest.fixture(scope="session", autouse=True)
def load_env(pytestconfig):
    environment = pytestconfig.getoption("env")
    
    env_file = f"config/config_{environment}.env"
    
    load_dotenv(dotenv_path=env_file)