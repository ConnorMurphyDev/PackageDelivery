# Connor Murphy         Student ID:001093925      WGU Data Structures and Algorithms 2 C950
from datetime import datetime, timedelta
import package


class Truck:
    def __init__(self):
        self.packages = []  # refers to package id numbers
        self.alreadyDelivered = []
        self.route = []
        self.mileage = 0
        self.departureTime = datetime.time





# Returns the distance between the delivery locations of two packages
# For info on how the distanceTable is structured, refer to cityDataImporter.py
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

    return float(distanceTable[package1Index][package2Index])





# Manually loads the trucks
def loadTrucks():
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()

    truck1.departureTime = timedelta(hours=8)
    truck2.departureTime = timedelta(hours=9, minutes=5)
    # truck 3's departure time is set in timeStatus, after truck 1 returns

    # Manually based of delivery requirements and relative location.
    truck1.packages = [1, 13, 14, 15, 16, 19,
                       20, 21, 29, 30, 31, 32, 34, 37, 39, 40]
    truck2.packages = [4, 6, 11, 17, 22, 23, 24, 25, 26, 28]
    truck3.packages = [2, 3, 5, 7, 8, 9, 10, 12, 18, 27, 33, 35, 36, 38]

    return truck1, truck2, truck3





# Decides the route thet truck will take
def decideRoute(truck, distanceMap, hashMap):

    # Fake package with Hub address for distance comparison
    tempHubPackage = package.Package
    tempHubPackage.address = "4001 South 700 East"

    # Values set higher than realalistic since we compare and replace with lower numbers.
    closestDelivery = 1000
    newDistance = 1000
    idTracker = 1000

    i = 0
    i2 = 0



    # Distance from hub to first package
    while(i < len(truck.packages)):
        newDistance = distanceBetween(
            tempHubPackage, hashMap.lookUp(truck.packages[i])[1], distanceMap)

        # If we have a new closest package its data is saved
        if(newDistance < closestDelivery):
            closestDelivery = newDistance
            idTracker = truck.packages[i]
        i = i + 1

    # Add first package to the planned route and its milage is recorded
    truck.route.append(idTracker)
    truck.mileage = closestDelivery
    hashMap.lookUp(idTracker)[1].deliveryMiles = truck.mileage
    i = 0
    closestDelivery = 1000



    # Find each sequential clostest next delivery, Excludes already visited locations, repeats until none are left.
    while(i2 < len(truck.packages) - 1):

        while(i < len(truck.packages)):

            if(truck.packages[i] not in truck.route):

                # The -1 gives the last item in the list
                newDistance = distanceBetween(hashMap.lookUp(
                    truck.route[-1])[1], hashMap.lookUp(truck.packages[i])[1], distanceMap)

                if(newDistance < closestDelivery):
                    closestDelivery = newDistance
                    idTracker = truck.packages[i]
            i = i + 1

        # Adds to trucks route, updates milage, updates index counters
        truck.route.append(idTracker)
        truck.mileage = truck.mileage + closestDelivery
        hashMap.lookUp(idTracker)[1].deliveryMiles = truck.mileage
        closestDelivery = 1000
        i2 = i2 + 1
        i = 0




    # Adds mileage for distance between final delivery and return to the hub
    newDistance = distanceBetween(hashMap.lookUp(
        truck.route[-1])[1], tempHubPackage, distanceMap)
    truck.mileage = truck.mileage + newDistance

"""
While no code was quoted, or paraphrased. The Ideas and insperation for this segment was sourced from:

Lawrence, Weru. (2021) Stem Lounge Algorithms for the Traveling Salesman Problem
https://stemlounge.com/animated-algorithms-for-the-traveling-salesman-problem/


Pamela, Fox. (2020) Solving Hard Problems using heuristics
https://www.khanacademy.org/computing/ap-computer-science-principles/algorithms-101/solving-hard-problems/a/using-heuristics
"""