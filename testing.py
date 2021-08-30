from timeStatus import deliveredAt, deliveryList, userInterface
from hashMap import HashMap
import csv
import packageDataImporter
from graph import Vertex
import package
import cityDataImporter
import truck
from datetime import datetime, timedelta
""" from <module> import <Class>  self notes. remove this later"""





truck1, truck2, truck3 = truck.loadTrucks()


testHashMap = packageDataImporter.populateHashMap()

testDistanceTable = cityDataImporter.readCSV()

truck.decideRoute(truck1, testDistanceTable, testHashMap)

truck.decideRoute(truck2, testDistanceTable, testHashMap)

truck.decideRoute(truck3, testDistanceTable, testHashMap)


deliveredAt(testHashMap, truck1, truck2, truck3)







string = "08:55"

userInterface(testHashMap, truck1, truck2, truck3)



"""
time = datetime.time

time = timedelta(hours = 15)
print(time)


time =  time + timedelta(minutes = 45)
print(time)

print(time)
"""
#print(testHashMap)
#print(testDistanceTable)



#print(truck.distanceBetween(testHashMap.map[13][1], testHashMap.map[0][1], testDistanceTable))