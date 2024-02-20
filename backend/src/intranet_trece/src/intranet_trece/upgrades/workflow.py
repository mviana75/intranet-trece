from intranet_trece import logger
from plone import api
from Products.CMFPlone.WorkflowTool import WorkflowTool


def atualiza_permissoes(context):
    """Atualiza todas as permissões em vista do novo workflow."""
    # Utilizamos a tool que gerencia todos os workflows
    wf_tool: WorkflowTool = api.portal.get_tool("portal_workflow")
    # Atualiza permissões
    wf_tool.updateRoleMappings()
    # Loga que modificação foi realizada
    logger.info("Permissões de workflow atualizadas")
