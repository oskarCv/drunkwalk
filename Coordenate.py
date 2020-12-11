
class Coordenate:
    #Constructor method
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #Perform the Move Action returns a new Coordenate
    def move(self,deltaX,deltaY):
        return Coordenate(self.x + deltaX, self.y+deltaY)
    
    def calculateDistance(self, controlCoordinate):
        deltaX = self.x - controlCoordinate.x
        deltaY = self.y - controlCoordinate.y
        return (deltaX**2+ deltaY**2)**0.5
    