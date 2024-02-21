from intranet_trece import logger
from plone import api


def alterar_permissionamento_estrutura(context):
    portal = api.portal.get()
    estrutura = portal["estrutura"]
    permission_id = "intranet_trece: Add Area"
    roles = [
        "Contributor",
        "Editor",
        "Manager",
        "Site Administrator",
    ]
    estrutura.manage_permission(permission_id, roles=roles)
    logger.info(f"Alterado permissionamento em {estrutura}.")
