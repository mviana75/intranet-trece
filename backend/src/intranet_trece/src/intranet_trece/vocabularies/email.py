from intranet_trece import _
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


TIPOS = [
    ("corporativo", _("Corporativo")),
    ("pessoal", _("Pessoal")),
    ("outro", _("Outro")),
]


@provider(IVocabularyFactory)
def tipos_vocabulary(context):
    """Vocabulário de possíveis tipos de email."""
    terms = []
    for id_, title in TIPOS:
        terms.append(SimpleTerm(id_, id_, title))
    return SimpleVocabulary(terms)
