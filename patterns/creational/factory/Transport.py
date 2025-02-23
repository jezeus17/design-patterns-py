from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass
