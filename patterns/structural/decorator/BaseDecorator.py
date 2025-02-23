

from Notifier import Notifier


class BaseDecorator(Notifier):
    def send(self, message: str):
        self.notifier.send(message)

    def __init__(self, notifier: Notifier):
        self.notifier = notifier
