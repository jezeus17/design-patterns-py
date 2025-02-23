

from House import House


class HouseBuilder:
    
    def __init__(self):
        self.house = House()
        
    def buildWalls(self):
        self.house.walls = "concrete walls"
    
    def buildRoof(self):
        self.house.roof = "wooden roof"
        
    def returnHouse(self):
        return self.house