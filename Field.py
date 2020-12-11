
class Field:
    def __init__(self):
        # define a Dictionary to keep trak of the drunks
        self.drunksCoordinates = {}
    
    def addDrunk(self, drunk, coordinate):
        self.drunksCoordinates[drunk]=coordinate

    
    def moveDrunk(self, drunk):
        deltaX, deltaY = drunk.walkSteps()
        currentCoordinate= self.drunksCoordinates[drunk]
        newCoordinate= currentCoordinate.move(deltaX, deltaY)

        self.drunksCoordinates[drunk]=newCoordinate

    def getCoordinate(self, drunk):
        return self.drunksCoordinates[drunk]