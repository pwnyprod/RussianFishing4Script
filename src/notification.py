import logging
from abc import abstractmethod, ABC

from notification_provider.abstract_messaging_method import MessagingMethod
from notification_provider.discord_method import DiscordMethod
from notification_provider.email_method import EmailMethod
from notification_provider.miaotixing_method import MiaotixingMethod
from notification_provider.null_method import NullMethod
from notification_provider.plot_method import PlotMethod
from setting import Setting
from timer import Timer

logger = logging.getLogger(__name__)

class Notification:
    """A class that is responsible for sending notifications to the user."""
    setting: Setting
    method: str | None

    def __init__(self, settings: Setting):
        self.setting = settings
        self.recipient = settings.recipient
        self.method = settings.method

    # pylint: disable=too-many-public-methods
    @staticmethod
    def get_messaging_method(self, timer: Timer) -> MessagingMethod:
        if self.method == "email":
            return EmailMethod(self.recipient)
        elif self.method == "discord":
            return DiscordMethod(self.recipient)
        elif self.method == "miaotixing":
            return MiaotixingMethod()
        elif self.method == "plot":
            return PlotMethod(timer)
        else:
            return NullMethod()