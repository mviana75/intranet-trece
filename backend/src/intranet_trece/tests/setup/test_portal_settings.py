"""Portal settings tests."""
from plone import api

import pytest


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    @pytest.mark.parametrize(
            "setting,expected",
            [
                ["plone.default_language", "pt-br"],
                ["plone.email_charset", "utf-8"],
                ["plone.email_from_address", None],
                ["plone.email_from_name", "Nova - Intranet TRE-CE"],
                ["plone.enable_sitemap", False],
                ["plone.portal_timezone", "America/Fortaleza"],
                ["plone.site_title", "Nova Intranet TRE-CE"],
                ["plone.smtp_host", "smtp.tre-ce.jus.brrrrrrr"],
                ["plone.smtp_port", 99],
                ["plone.twitter_username", "trece_twitter"],
            ]
    )
    def test_portal_settings(self, portal, setting, expected):
        """Test portal settings."""
        value = api.portal.get_registry_record(setting)
        assert value == expected, f"Valor incorreto para {setting} ({value})"