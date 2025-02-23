
from Factory import Factory
from Ship import Ship


class MaritimeFactory(Factory):
    def create(self):
        return Ship()