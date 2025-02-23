from BaseDecorator import BaseDecorator


class SMSDecorator(BaseDecorator):

    def send(self, message: str):
        self.notifier.send(message)
        print("sent via sms: " + message)
