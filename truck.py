import package

class truck:
    def __init__(self):
        self.packages
        self.alreadyDelivered
        self.route = [None]
        self.mileage = 0



def distanceBetween(package1, package2, distanceTable):
    
    package1Index = 0
    package2Index = 0

    i = 0
    while(i < len(distanceTable)):
        if package1.address == distanceTable[0][i]:
            package1Index = i


    i = 0
    while(i < len(distanceTable)):
        if package2.address == distanceTable[0][i]:
            package2Index = i

    return distanceTable[package1Index][package2Index]


