from abc import abstractmethod, ABC


class MessagingMethod(ABC):
    @abstractmethod
    def send_message(self, message: str):
        pass