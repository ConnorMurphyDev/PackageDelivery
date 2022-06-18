# Connor Murphy         Student ID:001093925      WGU Data Structures and Algorithms 2 C950
#Reads package data from a CSV file and populates the hashmap

import csv
from hashMap import HashMap
from package import Package

packageFile = "packageFile.csv"
  



#Reads package data
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
  
        rowCount = csvreader.line_num

    return rows, rowCount



#Populates the hasmap with packages
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
