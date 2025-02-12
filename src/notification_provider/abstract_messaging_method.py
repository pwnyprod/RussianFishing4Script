from abc import abstractmethod, ABC


class MessagingMethod(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def send_message(self, message: str):
        pass