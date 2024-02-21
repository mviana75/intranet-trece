from intranet_trece import logger
from intranet_trece.content.area import Area
from zope.lifecycleevent import ObjectAddedEvent


def _update_excluded_from_nav(obj: Area):
    """Update excluded_from_nav in the Area object."""
    description = obj.description
    obj.exclude_from_nav = False if description else True
    logger.info(f"Atualizado o campo excluded_from_nav para {obj.title}")


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Area."""
    _update_excluded_from_nav(obj)
