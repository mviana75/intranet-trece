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


@implementer(IArea)
class Area(Container):
    """Área no TRE-CE."""
