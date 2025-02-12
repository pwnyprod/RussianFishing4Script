from notification_provider.abstract_messaging_method import MessagingMethod


class NullMethod(MessagingMethod):
    def __init__(self):
        pass

    def send_message(self, message: str):
        # Implement Gmail sending logic here
        pass