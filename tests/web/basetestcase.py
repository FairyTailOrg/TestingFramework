import os

import pytest

from custom_lib.web_lib import LoginPage
from lib.logger_config import setup_logger


class BaseTestCase:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
        self.login = LoginPage(self.page)
        self.logger = setup_logger()
        self.existent_patient_username = os.getenv("EXISTENTPATIENT_USER")
        self.existent_patient_password = os.getenv("EXISTENTPATIENT_PASSWORD")
