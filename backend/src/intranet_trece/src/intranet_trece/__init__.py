"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "intranet_trece"

_ = MessageFactory("intranet_trece")

logger = logging.getLogger("intranet_trece")
