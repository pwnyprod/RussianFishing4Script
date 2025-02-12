from notification_provider.abstract_messaging_method import MessagingMethod


class DiscordMethod(MessagingMethod):
    def __init__(self):
        pass

    def send_message(self, message: str):
        # Implement Discord sending logic here
        pass