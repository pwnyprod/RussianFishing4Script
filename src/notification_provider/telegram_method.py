from notification_provider.abstract_messaging_method import MessagingMethod


class TelegramMethod(MessagingMethod):
    def send_message(self, message: str):
        # Implement Telegram sending logic here
        pass