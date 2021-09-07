# Connor Murphy         Student ID:001093925      WGU Data Structures and Algorithms 2 C950

from timeStatus import deliveredAt, userInterface
import packageDataImporter
import cityDataImporter
import truck



# Trucks are manually loaded with their packages
truck1, truck2, truck3 = truck.loadTrucks()



# The hashMap is populated will all of the packages and a 2d list of the distances is loaded in.
hashMap = packageDataImporter.populateHashMap()
distanceTable = cityDataImporter.readCSV()



# The list of packages on each truck is organized into a more efficient delivery path
truck.decideRoute(truck1, distanceTable, hashMap)
truck.decideRoute(truck2, distanceTable, hashMap)
truck.decideRoute(truck3, distanceTable, hashMap)



# The time each package is delivered is calculated and saved. From timeStatus.py
deliveredAt(hashMap, truck1, truck2, truck3)



# Delivery stats are presented and a loop requesting a time for delivery information is started until the user types EXIT. From timeStatus.py
userInterface(hashMap, truck1, truck2, truck3)