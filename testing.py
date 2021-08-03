from hashMap import hashMap
import csv
import packageDataImporter
from graph import Vertex
import package

# newMap = packageDataImporter.populateHashMap()
# populate the hashmap


#map = packageDataImporter.populateHashMap()

#print("some or the other")



testPackage = package

testPackage.packageID = 1
testPackage.address = "butts"
testPackage.weight = 5

print(testPackage)


"""
packageFile = "packageFile.csv"
  

#fields = []
rows = []


with open(packageFile, 'r') as csvfile:
 
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    #fields = next(csvreader)
    next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
  
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
  

"""



"""
testHashMap = hashMap()


testHashMap.insert(10, 'butts')

print(testHashMap.lookUp(10))
"""



"""
mylist = [None] * 5

mylist[0] = 'first spot', 'butt', ' hi'
mylist[1] = 'second spot'
mylist[2] = 'third spot'
mylist[3] = 'fourth spot'
mylist[4] = 'fifth spot'


print(mylist)
"""