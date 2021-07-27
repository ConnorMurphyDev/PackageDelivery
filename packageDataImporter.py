#Connor Murphy
# Reads package data from a CSV file and populates the hashmap

import csv
from hashMap import hashMap

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
        newHashMap.insert(rows[i][0], rows[i])
        i +=1
    
    return newHashMap



