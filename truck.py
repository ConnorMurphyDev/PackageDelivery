from datetime import datetime, timedelta
import package

class Truck:
    def __init__(self):
        self.packages = [] #refers to package id numbers
        self.alreadyDelivered = []
        self.route = []
        self.mileage = 0
        self.departureTime = datetime.time






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

    #Converted to float before sending out
    return float(distanceTable[package1Index][package2Index])





#call to initialize and return trucks with their proper packages
def loadTrucks():
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()

    #Truck 1 leaves at 8AM, truck 2 leaves at 9:05AM when packages arrive, truck 3 leaves when truck 1 returns. will be set in the deliveredAt method in timeStatus
    truck1.departureTime = timedelta(hours = 8)
    truck2.departureTime = timedelta(hours = 9, minutes = 5)
    #truck3.departureTime = timedelta(hours = 8)              ADD IN TIME STATUS WHEN TRUCK 1 RETURNS


    #Truck 1 is the first to leave at 8am, while truck 2 waits for the late packages and leaves
    #at 9:05. Followed by truck 3 leaving after truck 1 returns. These packages were loaded
    #manually based of delivery requirements and relative location.
    truck1.packages = [1, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 32, 34, 37, 39, 40]
    truck2.packages = [4, 6, 11, 17, 22, 23, 24, 25, 26, 28]
    truck3.packages = [2, 3, 5, 7, 8, 9, 10, 12, 18, 27, 33, 35, 36, 38]

    truck1.departureTime



    #decideRoute(truck1)




    return truck1, truck2, truck3



#Decides the route thet truck will take
#Since the hub is hard coded, for different cities this would need to be changed
def decideRoute(truck, distanceMap, hashMap):

    tempHubPackage = package.Package
    tempHubPackage.address = "4001 South 700 East"
    closestDelivery = 1000000
    newDistance = 1000000
    idTracker = 1000000
    i = 0
    i2 = 0

    #Initial distance from HUB
    while(i < len(truck.packages)):

        #newDistance = distanceBetween(tempHubPackage, hashMap.map[hashMap.lookUp(i)][1], distanceMap)
        #newDistance = distanceBetween(tempHubPackage, hashMap.lookUp(i)[1], distanceMap)
        newDistance = distanceBetween(tempHubPackage, hashMap.lookUp(truck.packages[i])[1], distanceMap)


        if( newDistance < closestDelivery):
            closestDelivery = newDistance
            idTracker = truck.packages[i]
        i = i + 1

    truck.route.append(idTracker)
    truck.mileage = closestDelivery
    hashMap.lookUp(idTracker)[1].deliveryMiles = truck.mileage
    i = 0
    closestDelivery = 1000000


    #All trips between after inital and before final hub visit
    while(i2 < len(truck.packages) - 1):

        while(i < len(truck.packages)):

            if(truck.packages[i] not in truck.route):
                
                #The -1 gives the last item in the list
                newDistance = distanceBetween(hashMap.lookUp(truck.route[-1])[1], hashMap.lookUp(truck.packages[i])[1], distanceMap)


                if( newDistance < closestDelivery):
                    closestDelivery = newDistance
                    idTracker = truck.packages[i]
            i = i + 1

        truck.route.append(idTracker)
        truck.mileage = truck.mileage + closestDelivery
        hashMap.lookUp(idTracker)[1].deliveryMiles = truck.mileage
        closestDelivery = 1000000
        i2 = i2 + 1
        i = 0
    



    #Adds mileage for distance between final delivery and return to the hub
    newDistance = distanceBetween(hashMap.lookUp(truck.route[-1])[1], tempHubPackage, distanceMap)
    truck.mileage = truck.mileage + newDistance




    #print(truck.route)