#Connor Murphy
# Reads City Distnace data from a CSV file and populates a weighted graph

import csv

distanceFile = "DistanceTable.csv"
  




# Make better variable names?
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

    return rows #, rowCount