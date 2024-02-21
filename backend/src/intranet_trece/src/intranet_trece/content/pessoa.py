from intranet_trece import _
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.supermodel.model import Schema
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer


class IPessoa(Schema):
    """Definição de uma pessoa no TRE-CE."""

    title = schema.TextLine(title=_("Nome Completo"), required=True)
    description = schema.Text(title=_("Biografia"), required=False)

    model.fieldset(
        "estrutura",
        _("Estrutura"),
        fields=[
            "cargo",
            "area",
        ],
    )
    cargo = schema.TextLine(title="Cargo", required=True)
    area = RelationList(
        title="Área",
        required=False,
        default=[],
        value_type=RelationChoice(
            title="Área", vocabulary=StaticCatalogVocabulary({"portal_type": ["Area"]})
        ),
    )


@implementer(IPessoa)
class Pessoa(Container):
    """Uma pessoa no TRE-CE."""
