"""
Module for Messaging related methods.
"""

# pylint: disable=missing-function-docstring
# docstring for every functions? u serious?

import logging
from abc import abstractmethod, ABC

from notification_provider.abstract_messaging_method import MessagingMethod
from notification_provider.discord_method import DiscordMethod
from notification_provider.email_method import EmailMethod
from notification_provider.null_method import NullMethod
from notification_provider.telegram_method import TelegramMethod
from setting import Setting

logger = logging.getLogger(__name__)

class Notification:
    """A class that is responsible for sending notifications to the user."""
    setting: Setting
    method: str | None

    def __init__(self, settings: Setting):
        self.setting = settings
        self.recipient = settings.recipient

    # pylint: disable=too-many-public-methods
    @staticmethod
    def get_messaging_method(self) -> MessagingMethod:
        if self.method == "email":
            return EmailMethod(self.recipient)
        elif self.method == "discord":
            return DiscordMethod(self.recipient)
        elif self.method == "telegram":
            return TelegramMethod(self.recipient)
        else:
            return NullMethod()