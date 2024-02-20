from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer


class IPessoa(Schema):
    """Definição de uma pessoa no TRE-CE."""

    # Informações básicas
    title = schema.TextLine(title="Nome Completo", required=True)
    description = schema.Text(title="Biografia", required=False)

    # Estrutura
    cargo = schema.TextLine(title="Cargo", required=True)
    area = RelationList(
        title="Área",
        required=False,
        default=[],
        value_type=RelationChoice(
            title="Área", vocabulary=StaticCatalogVocabulary({"portal_type": ["Area"]})
        ),
    )

    # Contato
    email = schema.TextLine(title="E-mail", required=True)
    ramal = schema.TextLine(title="Ramal", required=True)


@implementer(IPessoa)
class Pessoa(Container):
    """Uma pessoa no TRE-CE."""
