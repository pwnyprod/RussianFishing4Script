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
from notification_provider.gmail_method import GmailMethod
from notification_provider.telegram_method import TelegramMethod
from setting import Setting

logger = logging.getLogger(__name__)

class Notification:
    """A class that is responsible for sending notifications to the user."""

    # pylint: disable=too-many-public-methods
    @staticmethod
    def get_messaging_method(method: str) -> MessagingMethod:
        if method == "email":
            return EmailMethod()
        elif method == "gmail":
            return GmailMethod()
        elif method == "discord":
            return DiscordMethod()
        elif method == "telegram":
            return TelegramMethod()
        else:
            raise ValueError(f"Unknown messaging method: {method}")