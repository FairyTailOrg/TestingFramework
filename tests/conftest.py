"""Configuration file to configure the proper tests."""
import base64
import os

import pytest
import pytest_html
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright
from pytest_html_reporter import attach

from lib.logger_config import logger


@pytest.fixture(scope="session")
def playwright():
    """Initialize the playwright lib.

    Yields:
        _type_: _description_
    """
    with sync_playwright() as p:
        yield p


@pytest.fixture
def log():
    """Instance of logger.

    Returns:
        logger: logger instanced and initialized.
    """
    return logger


@pytest.fixture(scope="function")
def browser(playwright, pytestconfig, browser_names, log):
    """Browser instance from browser params.

    Args:
        playwright (_type_): playwright instance.
        pytestconfig (_type_): pytest class.
        browser_names (list): browser list.

    Returns:
        _type_: playwright.browser instance.
    """
    browser = getattr(
        playwright,
        browser_names
        ).launch(headless=pytestconfig.getoption("headless"))
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def mobile_browser(playwright, pytestconfig, browser_names):
    """Browser instance from mobile browser params.

    Args:
        playwright (_type_): playwright instance.
        pytestconfig (_type_): pytest class.

    Returns:
        _type_: playwright.browser instance.
    """
    # Use Playwright to launch a browser
    if browser_names == 'firefox':
        pytest.skip("There are not support in Firefox for mobile browsers.")

    browser = getattr(
        playwright,
        browser_names,
        ).launch(headless=pytestconfig.getoption("headless"))
    # Define the iPhone 13 emulation settings
    iPhone_13 = playwright.devices['iPhone 13']
    # Create a new browser context with the iPhone 13 emulation
    context = browser.new_context(**iPhone_13)
    # Create a new page in the context
    page = context.new_page()
    yield page
    # Clean up
    page.close()
    context.close()
    browser.close()


def pytest_generate_tests(metafunc):
    """Configure pytest test execution.

    Args:
        metafunc (_type_): pytest class.
    """
    browser_list = ["chromium", "firefox", "webkit"]
    if ("browser" in metafunc.fixturenames and
            metafunc.config.getoption("browser") == "all"):
        metafunc.parametrize("browser_names", browser_list)
    elif ("browser" in metafunc.fixturenames and
            metafunc.config.getoption("browser") in browser_list):
        metafunc.parametrize(
            "browser_names",
            [metafunc.config.getoption("browser")]
            )


@pytest.fixture(scope="function")
def page(browser):
    """Page instance from playwright."""
    context = browser.new_context()
    page = context.new_page()
    yield page

    page.close()
    context.close()


def create_screenshots_dir():
    """Screenshots path to save the screenshot taken when a test failes.

    Returns:
        str: screenshot path.
    """
    screenshots_dir = 'results/screenshots'
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    return screenshots_dir


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Configure the pytest report.

    Args:
        item (_type_): pytest class.
        call (_type_): pytest class.
    """
    pytest_html_report = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        xfail = hasattr(report, "wasxfail")
        if report.failed or xfail and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshots_dir = create_screenshots_dir()
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            screenshot_bytes = page.screenshot(path=screenshot_path)

        if (report.skipped and xfail) or (report.failed and not xfail):
            attach(data=page.screenshot(path=screenshot_path))
            extra.append(pytest_html_report.extras.image(
                base64.b64encode(screenshot_bytes).decode())
                )
            extra.append(pytest_html_report.extras.html('<div></div>'))

        report.extras = extra


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """To get the specific args for playwright browser.

    Args:
        browser_context_args (_type_): Browser args.

    Returns:
        _type_: screenshot file taken.
    """
    return {
        **browser_context_args,
        'record_video_dir': create_screenshots_dir()
        }


def pytest_addoption(parser):
    """Parameters in line.

    Args:
        parser (parser): method to get the command line args.
    """
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against"
        )
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Select specific browser"
        )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Choose if headless or not"
        )
    parser.addoption(
        "--mobile",
        action="store",
        default="",
        help="Select a specific mobile to execute this."
        )


@pytest.fixture(scope="session", autouse=True)
def load_env(pytestconfig):
    """Get the env file and load it to use it in tests.

    Args:
        pytestconfig (pytestconfig): pytestconfiguration class.
    """
    environment = pytestconfig.getoption("env")

    env_file = f"config/config_{environment}.env"

    load_dotenv(dotenv_path=env_file)