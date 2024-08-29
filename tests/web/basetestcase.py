"""This will get all the configurations for web tests."""
import os

import pytest

from custom_lib.web_lib import HomePage
from lib.logger_config import logger


class BaseTestCase:
    """Base test cae web tests class."""

    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Initialize of the web tests."""
        self.page = page
        self.home = HomePage(self.page)
        self.logger = logger
        self.existent_patient_username = os.getenv("QAUSER")
        self.existent_patient_password = os.getenv("QAPASSWORD")
