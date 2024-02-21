from intranet_trece import PACKAGE_NAME
from zope.schema.vocabulary import SimpleVocabulary

import pytest


class TestVocabTiposEmail:

    name = f"{PACKAGE_NAME}.tipos_email"

    @pytest.fixture(autouse=True)
    def _vocab(self, get_vocabulary, portal):
        self.vocab = get_vocabulary(self.name, portal)

    def test_vocabulary(self):
        assert self.vocab is not None
        assert isinstance(self.vocab, SimpleVocabulary)

    @pytest.mark.parametrize(
        "token",
        [
            "corporativo",
            "pessoal",
            "outro",
        ],
    )
    def test_token(self, token):
        assert token in [x for x in self.vocab.by_token]
