from intranet_trece.content.pessoa import Pessoa
from plone import api
from plone.dexterity.fti import DexterityFTI
from zope.component import createObject

import pytest


CONTENT_TYPE = "Pessoa"


@pytest.fixture
def payload() -> dict:
    """Payload to create a new Pessoa."""
    return {
        "type": CONTENT_TYPE,
        "title": "Alex Limi",
        "description": "Criador do Plone",
        "email": "limi@plone.org",
        "ramal": "1975",
        "id": "alex-limi",
    }


class TestPessoa:
    @pytest.fixture(autouse=True)
    def _fti(self, get_fti, integration):
        self.fti = get_fti(CONTENT_TYPE)

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    def test_factory(self):
        factory = self.fti.factory
        obj = createObject(factory)
        assert obj is not None
        assert isinstance(obj, Pessoa)

    @pytest.mark.parametrize(
        "behavior",
        [
            "plone.namefromtitle",
            "plone.leadimage",
            "plone.shortname",
            "plone.excludefromnavigation",
            "plone.versioning",
        ],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)

    @pytest.mark.parametrize(
        "roles",
        [
            ["Manager"],
            ["Editor"],
            ["Contributor"],
            ["Site Administrator"],
        ]
    )
    def test_cant_create_outsite_colaboradores(self, portal, payload, roles):
        from AccessControl.unauthorized import Unauthorized

        with pytest.raises(Unauthorized) as exc:
            with api.env.adopt_roles(roles):
                api.content.create(container=portal, **payload)
        assert "Cannot create Pessoa" in str(exc)

    @pytest.mark.parametrize(
        "roles",
        [
            ["Manager"],
            ["Editor"],
            ["Contributor"],
            ["Site Administrator"],
        ]
    )
    def test_create_inside_colaboradores(self, portal, payload, roles):
        container = portal["colaboradores"]
        with api.env.adopt_roles(roles):
            content = api.content.create(container=container, **payload)
        assert content.portal_type == CONTENT_TYPE
        assert isinstance(content, Pessoa)