from notification_provider.abstract_messaging_method import MessagingMethod


class TelegramMethod(MessagingMethod):
    def __init__(self):
        pass

    def send_message(self, message: str):
        # Implement Telegram sending logic here
        pass