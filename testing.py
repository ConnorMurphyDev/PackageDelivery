from hashMap import hashMap
import csv
import packageDataImporter
from graph import Vertex
import package
import cityDataImporter
import truck






testHashMap = packageDataImporter.populateHashMap()

testDistanceTable = cityDataImporter.readCSV()


print(testHashMap)
print(testDistanceTable)


print("we did it")


if testHashMap.map[0][1].address == testDistanceTable[0][19]:
    print("They are equal")


print(truck.distanceBetween(testHashMap.map[0][1], testHashMap.map[5][1], testDistanceTable))