import pytest

from tests.web.basetestcase import BaseTestCase


class TestLogin(BaseTestCase):
    @pytest.mark.smoke
    @pytest.mark.web
    def test_valid_login(self):
        assert self.home.login(
            self.existent_patient_username, self.existent_patient_password)