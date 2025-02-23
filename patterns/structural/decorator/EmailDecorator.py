

from BaseDecorator import BaseDecorator


class EmailDecorator(BaseDecorator):

    def send(self, message: str):
        self.notifier.send(message)
        print("sent via email: " + message)
