from intranet_trece import validadores

import pytest


@pytest.mark.parametrize(
    "value,expected",
    [
        ["1@tre-ce.jus.br", True],
        ["foobar@tre-ce.jus.br", True],
        ["bar-foo@tre-ce.jus.br", True],
        ["1@tre-ce.jus.br.br", False],
        ["foobar@tre-ce.jus.br.br", False],
        ["bar-foo@tre-ce.jus.br.br", False],
        ["ericof@simplesconsultoria.com.br", False],
    ]
)
def test_is_valid_email(value, expected):
    """Testa a função is_valid_email."""
    assert validadores.is_valid_email(value) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ["1234", True],
        ["4321", True],
        ["9234", True],
        [" ", False],
        ["12.34", False],
        ["HOLA", False],
        ["d1234", False],
        ["1234d", False],
    ]
)
def test_is_valid_extension(value, expected):
    """Testa a função is_valid_extension."""
    assert validadores.is_valid_extension(value) is expected