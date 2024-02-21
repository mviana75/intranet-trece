from intranet_trece import logger
from plone import api


def alterar_permissionamento_colaboradores(context):
    portal = api.portal.get()
    colaboradores = portal["colaboradores"]
    permission_id = "intranet_trece: Add Pessoa"
    roles = [
        "Contributor",
        "Editor",
        "Manager",
        "Site Administrator",
    ]
    colaboradores.manage_permission(permission_id, roles=roles)
    logger.info(f"Alterado permissionamento em {colaboradores}.")
