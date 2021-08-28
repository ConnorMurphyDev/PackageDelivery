from hashMap import HashMap
import csv
import packageDataImporter
from graph import Vertex
import package
import cityDataImporter
import truck
""" from <module> import <Class>  self notes. remove this later"""






print("hello everyone")

truck1, truck2, truck3 = truck.loadTrucks()


print(truck1.packages)









testHashMap = packageDataImporter.populateHashMap()

testDistanceTable = cityDataImporter.readCSV()

print("butts")
#print(testHashMap)
#print(testDistanceTable)



#print(truck.distanceBetween(testHashMap.map[13][1], testHashMap.map[0][1], testDistanceTable))