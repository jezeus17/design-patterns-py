from decorator.Notifier import Notifier
from decorator.SMSDecorator import SMSDecorator
from decorator.EmailDecorator import EmailDecorator


stack = Notifier()
stack = SMSDecorator(stack)
stack = EmailDecorator(stack)

stack.send("hello world!")
