from Drunk import TraditionalDrunk
from Field import Field
from Coordenate import Coordenate
from bokeh.plotting import figure, show

def walk_trip(field, drunk, steps):
    start = field.getCoordinate(drunk)
    for _ in range(steps):
        field.moveDrunk(drunk)
    return start.calculateDistance(field.getCoordinate(drunk))


def simulateWalk(steps, intentsNumber, drunkType):
    drunk= drunkType(name='Oskar')
    origin= Coordenate(0,0)
    distances=[]
    
    for _ in range(intentsNumber):
        field=Field()
        field.addDrunk(drunk,origin)
        walkSimulation = walk_trip(field, drunk, steps)
        distances.append(round(walkSimulation,1))
    return distances

def doGraph(x,y):
    graph = figure(title='Random Walk', x_axis_label='Steps',y_axis_label="Distance")
    graph.line(x,y, legend="Avrg Distance")
    show(graph)

def main(walkDistances,intentsNumber,drunkType):
    walk_avrg_distance = []
    for steps in walkDistances:
        distances = simulateWalk(steps,intentsNumber,drunkType)
        avgDistance =  round(sum(distances)/len(distances),4)
        maxDistance = max(distances)
        minDistance = min(distances)
        
        walk_avrg_distance.append(avgDistance)
        print(f'{drunkType.__name__} random walk {steps}')
        print(f'avrg {avgDistance}')
        print(f'max {maxDistance}')
        print(f'min {minDistance}')

    doGraph(walkDistances,walk_avrg_distance)

if __name__ == '__main__':
    walkDistances= [10,100,1000,10000]
    intentsNumber= 3
    

    main(walkDistances,intentsNumber,TraditionalDrunk)