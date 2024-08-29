import pytest

from tests.web.basetestcase import BaseTestCase


class TestHome(BaseTestCase):
    @pytest.mark.smoke
    @pytest.mark.api
    def test_home_headers(self):
        headers = self.home.check_utility_headers()
        assert headers[0] == 'Event Search'
        assert headers[1] == 'Find a Puppy'
        assert headers[2] == 'Register'
        assert headers[3] == 'Shop'
        assert headers[4] == 'AKC TV'
        assert headers[5] == 'AKC Rx'
