from notification_provider.abstract_messaging_method import MessagingMethod


class EmailMethod(MessagingMethod):
    def send_message(self, message: str):
        # Implement email sending logic here
        pass