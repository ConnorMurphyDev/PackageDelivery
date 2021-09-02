# Connor Murphy         Student ID:001093925      WGU Data Structures and Algorithms 2 C950
# Reads City Distnace data from a CSV file and populates a weighted graph

import csv

distanceFile = "DistanceTable.csv"
  



#Reads Distance Table into a 2d accessable list and returns it
def readCSV():
    rows = []
    rowCount = 0


    with open(distanceFile, 'r') as csvfile:
 
        csvreader = csv.reader(csvfile)
      
        
  
        # Adding each row to the list
        for row in csvreader:
            rows.append(row)
  
        # get total number of rows
        rowCount = csvreader.line_num

    return rows




"""
        Distance table format

BLANK    , ADDRESS 1   , ADDRESS 2   , ADDRESS 3   , ADDRESS 4

ADDRESS 1, DISTANCE 1 1, DISTANCE 2 1, DISTANCE 3 1, DISTANCE 4 1

ADDRESS 2, DISTANCE 1 2, DISTANCE 2 2, DISTANCE 3 2, DISTANCE 4 2

ADDRESS 3, DISTANCE 1 3, DISTANCE 2 3, DISTANCE 3 3, DISTANCE 4 3

ADDRESS 4, DISTANCE 1 4, DISTANCE 2 4, DISTANCE 3 4, DISTANCE 4 3


"""