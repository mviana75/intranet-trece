from intranet_trece import _
from intranet_trece import validadores
from plone.autoform.interfaces import IFormFieldProvider
from plone.schema.email import Email
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IContactInfo(model.Schema):
    """Informações de contato."""

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
        constraint=validadores.is_valid_email,
    )

    ramal = schema.TextLine(
        title=_(
            "Ramal",
        ),
        required=True,
        constraint=validadores.is_valid_extension,
    )
