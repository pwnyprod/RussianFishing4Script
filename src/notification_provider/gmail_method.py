from notification_provider.abstract_messaging_method import MessagingMethod


class GmailMethod(MessagingMethod):
    def send_message(self, message: str):
        # Implement Gmail sending logic here
        pass