#Connor Murphy
# Reads City Distnace data from a CSV file and populates a weighted graph

import csv
from graph import Vertex
from graph import Graph

distanceFile = "DistanceTable.csv"
  




# Make better variable names?
def readCSV():
    rows = []
    rowCount = 0


    with open(distanceFile, 'r') as csvfile:
 
        csvreader = csv.reader(csvfile)
      
        
        # Skips the headers row
        next(csvreader)
  
        # Adding each row to the list
        for row in csvreader:
            rows.append(row)
  
        # get total number of rows
        rowCount = csvreader.line_num

    return rows, rowCount



def makeVertexList():

    rows, rowCount = readCSV()
    list = []

    for i in range(0, rowCount - 1):
        list.append(Vertex(rows[i]))
    
    return rows, list, rowCount






def populateGraph():

    rowsCSV, vertexList, rowCount = makeVertexList()
    graph = Graph()

    #Cycles through each column
    for x in range(0, rowCount - 1):
        #Adds adds individual columns (as they get shorter and shorter)
        for i in range(x, rowCount - 1):
            graph.add_undirected_edge(vertexList[x], vertexList[i], rowsCSV[i][x + 1])





    
    return graph


newGraph = Graph()

newGraph.add_undirected_edge(Vertex("one"), Vertex("two"), 5)

print(newGraph)

print("test 1")

#newGraph = populateGraph()

#print(newGraph)

print("test 2")