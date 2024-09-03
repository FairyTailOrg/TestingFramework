import pytest

from tests.web.basetestcase import BaseTestCase


class TestLogin(BaseTestCase):
    @pytest.mark.smoke
    @pytest.mark.api
    def test_valid_login(self):
        assert not self.home.login(
            self.existent_patient_username, self.existent_patient_password)
