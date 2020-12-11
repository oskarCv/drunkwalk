import random

class Drunk:
    #constructor
    def __init__(self,name):
        self.name=name

#inherit from Drunk class
class TraditionalDrunk(Drunk):
    def __init__(self,name):
        #Parent class constructor call
        super().__init__(name)
    
    def walkSteps(self):
        #Random choise up, down, left, right
        return random.choice([(0,1),(0,-1),(-1,0),(1,0)])
