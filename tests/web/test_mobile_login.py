import pytest

from tests.web.basetestcase import BaseTestCase


class TestWebLogin(BaseTestCase):
    @pytest.mark.usefixtures("mobile_browser")
    @pytest.mark.smoke
    @pytest.mark.mobile
    def test_mobile(self, mobile_browser):
        mobile_browser.goto("https://example.com")
        assert "Example Domain" in mobile_browser.title()