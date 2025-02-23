
from HouseBuilder import HouseBuilder


houseBuilder = HouseBuilder()
house = houseBuilder.returnHouse()
house.checkState()
print('building....')

houseBuilder.buildRoof()
houseBuilder.buildWalls()
house.checkState()
