import os

import requests

from tests.api.basetestcase import BaseTestCase


class TestScheduling(BaseTestCase):
    def test_appt_reasons(self):
        url = os.getenv("SCHEDULING_URL")
        response = requests.get(url + "/appointments/reasons")
        assert response.status_code == 200
        data = response.json()
        assert self.api_lib.validate(data, self.scheduling.appt_reasons())