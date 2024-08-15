from tests.web.basetestcase import BaseTestCase


class TestLogin(BaseTestCase):
    def test_valid_login(self):
        assert self.login.login_existent_patient(self.existent_patient_username, self.existent_patient_password)