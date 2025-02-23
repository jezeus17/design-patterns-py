
from Truck import Truck
from Factory import Factory


class TerrestrialFactory(Factory):
    def create(self):
        return Truck()