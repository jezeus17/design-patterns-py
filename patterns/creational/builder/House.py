class House:
    
    def checkState(self):
        if hasattr(self,'walls'):
            print("walls:" + self.walls)
        else:
            print("no walls")
        if hasattr(self,'roof'):
            print("roof:" + self.roof)
        else:
            print("no roof")
