from intranet_trece import _
from zope.interface import Invalid

import re


class BadValue(Invalid):
    """Exception raised when a provided value is informed."""

    __doc__ = _("O valor está incorreto")


def validar_dados(data):
    """Validar dados informados pelo usuário."""
    value = data.email
    if not (value and is_valid_email(value)):
        raise BadValue(f"O email {value} não faz parte do domínio tre-ce.jus.br.")


def is_valid_email(value: str) -> bool:
    """Validar se o email é @tre-ce.jus.br."""
    has_match = True if value.endswith("@tre-ce.jus.br") else False
    return has_match if value else True


def is_valid_extension(value: str) -> bool:
    """Validar se o o ramal tem 4 dígitos numéricos."""
    has_match = True if re.match(r"^\d{4}$", value) else False
    return has_match if value else True
