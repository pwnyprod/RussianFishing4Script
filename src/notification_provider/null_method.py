import logging

from notification_provider.abstract_messaging_method import MessagingMethod

logger = logging.getLogger(__name__)
class NullMethod(MessagingMethod):
    def __init__(self):
        pass

    def send_message(self, message: str):
        logger.debug("Null method called, no message sent")
        pass