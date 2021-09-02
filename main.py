# Connor Murphy         Student ID:001093925      WGU Data Structures and Algorithms 2 C950

from timeStatus import deliveredAt, deliveryList, userInterface
from hashMap import HashMap
import csv
import packageDataImporter
from graph import Vertex
import package
import cityDataImporter
import truck
from datetime import datetime, timedelta



# Trucks are manually loaded with their packages
truck1, truck2, truck3 = truck.loadTrucks()



# The hashMap is populated will all of the packages and a 2d list of the distances is loaded in.
hashMap = packageDataImporter.populateHashMap()
distanceTable = cityDataImporter.readCSV()



# The list of packages on each truck is organized into a more efficient delivery path
truck.decideRoute(truck1, distanceTable, hashMap)
truck.decideRoute(truck2, distanceTable, hashMap)
truck.decideRoute(truck3, distanceTable, hashMap)



# The time each package is delivered is calculated and saved
deliveredAt(hashMap, truck1, truck2, truck3)



# Delivery stats are presented and a loop requesting a time for delivery information is started until the user types EXIT
userInterface(hashMap, truck1, truck2, truck3)





#GRAPH IS NOT USED. GET RID OF IT. UPDATE IMPORTS BEFORE SUBMITTING. GET RID OF ROWCOUNT IN CITYDATAIMPORTER