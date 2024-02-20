from intranet_trece import logger
from intranet_trece.setuphandlers.content import populate_portal
from plone import api


def cria_estrutura(context):
    portal = api.portal.get()
    populate_portal(
        portal,
        [
            "TRE-CE",
        ],
    )
    logger.info("Criadas conteúdos para organizar Áreas e Pessoas.")
