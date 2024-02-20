"""Portal settings tests."""
from plone import api


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    def test_portal_title(self, portal):
        """Test portal title."""
        value = api.portal.get_registry_record("plone.site_title")
        expected = "Nova Intranet TRE-CE"
        assert value == expected, f"Value '{value}' is not equal '{expected}'"