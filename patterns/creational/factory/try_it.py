from MaritimeFactory import MaritimeFactory
from TerrestrialFactory import TerrestrialFactory


terrestrialFactory = TerrestrialFactory()
maritimeFactory = MaritimeFactory()

truck = terrestrialFactory.create()
ship = maritimeFactory.create()

truck.deliver()
ship.deliver()
