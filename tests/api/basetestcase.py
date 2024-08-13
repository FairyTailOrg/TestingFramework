import os

import pytest

from custom_lib.schemas.types import Scheduling
from lib.api.api_lib import SchemaValidator
from lib.logger_config import setup_logger


class BaseTestCase:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.scheduling = Scheduling()
        self.logger = setup_logger()
        self.api_lib = SchemaValidator()
