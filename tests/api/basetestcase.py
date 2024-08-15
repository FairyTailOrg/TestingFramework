"""This will get all the configurations for api tests."""
import os

import pytest

from custom_lib.schemas.types import Scheduling
from lib.api.api_lib import SchemaValidator
from lib.logger_config import setup_logger


class BaseTestCase:
    """Base test cae api tests class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Initialize of the api tests."""
        self.url = os.getenv("SCHEDULING_URL")
        self.scheduling = Scheduling()
        self.logger = setup_logger()
        self.api_lib = SchemaValidator()
