from intranet_trece import logger
from intranet_trece.content.area import Area
from plone import api
from zope.lifecycleevent import ObjectAddedEvent
from zope.lifecycleevent import ObjectModifiedEvent


def _update_excluded_from_nav(obj: Area):
    """Update excluded_from_nav in the Area object."""
    description = obj.description
    obj.exclude_from_nav = False if description else True
    logger.info(f"Atualizado o campo excluded_from_nav para {obj.title}")


def _create_user_groups(obj: Area):
    """Create user group for area"""
    uuid = api.content.get_uuid(obj)
    groupname = f"{uuid}_editors"
    title = obj.title
    payload = {
        "groupname": groupname,
        "title": f"Editores para {title}",
        "description": f"Editores para a área {title} ",
    }
    editors = api.group.create(**payload)
    api.group.grant_roles(group=editors, roles=["Editor"], obj=obj)
    logger.info(
        f"Granted role of Editor to {uuid}_editors group on {obj.absolute_url()}"
    )


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Area."""
    _update_excluded_from_nav(obj)
    _create_user_groups(obj)


def modified(obj: Area, event: ObjectModifiedEvent):
    """Post modified handler for Area."""
    _update_excluded_from_nav(obj)
