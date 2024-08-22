"""This will get all the configurations for web tests."""
import os

import pytest

from custom_lib.web_lib import LoginPage
from lib.logger_config import logger


class BaseTestCase:
    """Base test cae web tests class."""

    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Initialize of the web tests."""
        self.page = page
        self.login = LoginPage(self.page)
        self.logger = logger
        self.existent_patient_username = os.getenv("EXISTENTPATIENT_USER")
        self.existent_patient_password = os.getenv("EXISTENTPATIENT_PASSWORD")
