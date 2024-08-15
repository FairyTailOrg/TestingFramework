import datetime
import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pytest_html_reporter import attach

from custom_lib.web_lib import LoginPage
from lib.logger_config import setup_logger


@pytest.fixture(scope="session")
def logger():
    return setup_logger()

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright, pytestconfig, browser_names):
    logger = setup_logger()
    logger.info(f"Browser instanced: {browser_names}")
    return getattr(playwright, browser_names).launch(headless=pytestconfig.getoption("headless"))

def pytest_generate_tests(metafunc):
    if "browser_names" in metafunc.fixturenames and metafunc.config.getoption("browser") == "all":
        metafunc.parametrize("browser_names", ["chromium", "firefox", "webkit"])
    elif "browser_names" in metafunc.fixturenames and metafunc.config.getoption("browser") in ["chromium", "firefox", "webkit"]:
        metafunc.parametrize("browser_names", [metafunc.config.getoption("browser")])

    

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page

    page.close()
    context.close()

def create_screenshots_dir():
    screenshots_dir = 'results/screenshots'
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    return screenshots_dir

# Fixture para tomar capturas de pantalla al fallar la prueba
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Este hook se ejecuta después de cada prueba
    outcome = yield
    report = outcome.get_result()

    # Solo tomar una captura de pantalla si la prueba falla
    if report.when == 'call' and report.failed:
        # Crear directorio de screenshots si no existe
        screenshots_dir = create_screenshots_dir()

        # Acceder a la página desde el fixture
        page = item.funcargs['page']

        # Guardar la captura de pantalla con el nombre del test
        screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
        #page.screenshot(path=screenshot_path)
        attach(data=page.screenshot(path=screenshot_path))
        print(f"Screenshot saved to {screenshot_path}")

# Este ejemplo asume que estás utilizando Playwright y que `page` es un fixture
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, 'record_video_dir': create_screenshots_dir()}

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Environment to run tests against")
    parser.addoption("--browser", action="store", default="chromium", help="Browser to execute the test, you can use: chromium, firefox, webkit or All(for the 3 mentioned before)")
    parser.addoption("--headless", action="store_true", default=False, help="Choose if headless or not")

@pytest.fixture(scope="session", autouse=True)
def load_env(pytestconfig):
    environment = pytestconfig.getoption("env")
    
    env_file = f"config/config_{environment}.env"
    
    load_dotenv(dotenv_path=env_file)