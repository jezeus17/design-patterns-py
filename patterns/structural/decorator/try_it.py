

from EmailDecorator import EmailDecorator
from Notifier import Notifier
from SMSDecorator import SMSDecorator


stack = Notifier()
stack = SMSDecorator(stack)
stack = EmailDecorator(stack)

stack.send("hello world!")