from intranet_trece import _
from intranet_trece import validadores
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import implementer
from zope.interface import invariant


class IArea(Schema):
    """Definição de uma Área no TRE-CE."""

    # Informações básicas
    title = schema.TextLine(title="Nome da Área", required=True)
    description = schema.Text(title="Descrição", required=False)

    model.fieldset(
        "contato",
        _("Contato"),
        fields=[
            "email",
            "ramal",
        ],
    )
    email = Email(
        title=_("Email"),
        required=True,
    )
    ramal = schema.TextLine(
        title=("Ramal"),
        required=True,
        constraint=validadores.is_valid_extension,
    )

    @invariant
    def validar_dados(data):
        """Validar dados enviados pelo usuário."""
        validadores.validar_dados(data)


@implementer(IArea)
class Area(Container):
    """Área no TRE-CE."""
