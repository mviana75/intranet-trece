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
            "tipo_email",
            "email",
            "ramal",
        ],
    )
    tipo_email = schema.Choice(
        title=_("Tipo de E-mail"),
        required=False,
        vocabulary="intranet_trece.tipos_email",
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
