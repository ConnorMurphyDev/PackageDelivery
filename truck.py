import package

class Truck:
    def __init__(self):
        self.packages = [] #refers to package id numbers
        self.alreadyDelivered = []
        self.route = []
        self.mileage = 0






#Returns the distance between the delivery locations of two packages
def distanceBetween(package1, package2, distanceTable):
    
    package1Index = 0
    package2Index = 0

    i = 0
    while(i < len(distanceTable)):
        if package1.address == distanceTable[0][i]:
            package1Index = i
        i = i + 1


    i = 0
    while(i < len(distanceTable)):
        if package2.address == distanceTable[0][i]:
            package2Index = i
        i = i + 1

    return distanceTable[package1Index][package2Index]





#call to initialize and return trucks with their proper packages
def loadTrucks():
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()

    #Truck 1 is the first to leave at 8am, while truck 2 waits for the late packages and leaves
    #at 9:05. Followed by truck 3 leaving after truck 1 returns. These packages were loaded
    #manually based of delivery requirements and relative location.
    truck1.packages = [1, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 32, 34, 37, 39]
    truck2.packages = [4, 6, 11, 17, 22, 23, 24, 25, 26, 28]
    truck3.packages = [2, 3, 5, 7, 8, 9, 10, 12, 18, 27, 33, 35, 36, 38]



    decideRoute(truck1)




    return truck1, truck2, truck3




def decideRoute(truck):

    truck.route.append(0) #start out at the hub. 0 references the hub on the distance table and