from hashMap import hashMap
import csv
import packageDataImporter
from graph import Vertex
import package
import cityDataImporter







testHashMap = packageDataImporter.populateHashMap()

testDistanceTable = cityDataImporter.readCSV()


print(testHashMap)
print(testDistanceTable)