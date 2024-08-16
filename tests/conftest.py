"""Configuration file to configure the proper tests."""
import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pytest_html_reporter import attach

from lib.logger_config import setup_logger


@pytest.fixture(scope="session")
def playwright():
    """Initialize the playwright lib.

    Yields:
        _type_: _description_
    """
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright, pytestconfig, browser_names):
    """Browser instance from browser params.

    Args:
        playwright (_type_): playwright instance.
        pytestconfig (_type_): pytest class.
        browser_names (list): browser list.

    Returns:
        _type_: playwright.browser instance.
    """
    logger = setup_logger()
    logger.info(f"Browser instanced: {browser_names}")
    return getattr(
        playwright,
        browser_names).launch(headless=pytestconfig.getoption("headless"))


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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Configure the pytest report.

    Args:
        item (_type_): pytest class.
        call (_type_): pytest class.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        screenshots_dir = create_screenshots_dir()

        page = item.funcargs['page']

        screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
        page.screenshot(path=screenshot_path)
        attach(data=page.screenshot(path=screenshot_path))
        print(f"Screenshot saved to {screenshot_path}")


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


@pytest.fixture(scope="session", autouse=True)
def load_env(pytestconfig):
    """Get the env file and load it to use it in tests.

    Args:
        pytestconfig (pytestconfig): pytestconfiguration class.
    """
    environment = pytestconfig.getoption("env")

    env_file = f"config/config_{environment}.env"

    load_dotenv(dotenv_path=env_file)
