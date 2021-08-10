#Connor Murphy
# Reads package data from a CSV file and populates the hashmap

import csv
from hashMap import hashMap
import package

packageFile = "packageFile.csv"
  




# Make better variable names?
def readCSV():
    rows = []
    rowCount = 0


    with open(packageFile, 'r') as csvfile:
 
        csvreader = csv.reader(csvfile)
      
        
        # Skips the headers row
        next(csvreader)
  
        # Adding each row to the list
        for row in csvreader:
            rows.append(row)
  
        # get total number of rows
        rowCount = csvreader.line_num

    return rows, rowCount




def populateHashMap():

    rows, rowCount = readCSV()
    i = 0

    newHashMap = hashMap()

    while i < rowCount - 1:

        tempPackage = package
        tempPackage.packageID = rows[i][0]
        tempPackage.address = rows[i][1]
        tempPackage.city = rows[i][2]
        tempPackage.state = rows[i][3]
        tempPackage.zipcode = rows[i][4]
        tempPackage.deliveryDeadline = rows[i][5]
        tempPackage.weight = rows[i][6]
        tempPackage.specialNotes = rows[i][7]



        newHashMap.insert(tempPackage.packageID, tempPackage)
        i +=1
    
    return newHashMap
