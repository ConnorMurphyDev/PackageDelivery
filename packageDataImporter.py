#Connor Murphy
# Reads package data from a CSV file and populates the hashmap

import csv
from hashMap import HashMap
from package import Package

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



#Call this to populate the hasmap of packages
def populateHashMap():

    rows, rowCount = readCSV()
    i = 0

    newHashMap = HashMap()
    tempPackage = [None] * rowCount #new



    while i < rowCount - 1:

        tempPackage[i] = Package()
        tempPackage[i].packageID = rows[i][0]
        tempPackage[i].address = rows[i][1]
        tempPackage[i].city = rows[i][2]
        tempPackage[i].state = rows[i][3]
        tempPackage[i].zipcode = rows[i][4]
        tempPackage[i].deliveryDeadline = rows[i][5]
        tempPackage[i].weight = rows[i][6]
        tempPackage[i].specialNotes = rows[i][7]



        newHashMap.insert(tempPackage[i].packageID, tempPackage[i])
        i +=1
    
    return newHashMap
