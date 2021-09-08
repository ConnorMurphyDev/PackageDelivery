# Connor Murphy         Student ID:001093925      WGU Data Structures and Algorithms 2 C950
from datetime import timedelta



#Set a delivery time for each package based off truck travel speed and distance traveled
def deliveredAt(hashMap, truck1, truck2, truck3):

    i = 0
    while(i < hashMap.size):

        if(hashMap.map[i]):
            #Without the departure time added yet, we are adding minutes to the delivery time
            hashMap.map[i][1].deliveryTime = timedelta(minutes = (hashMap.map[i][1].deliveryMiles / 0.3)) # 0.3 is miles per minute, instead of 18 MPH

            i = i + 1



    #Adjusting delivery times for the departure of truck 1, leaves at 8AM
    i = 0
    while(i < len(truck1.packages)):
        hashMap.lookUp(truck1.packages[i])[1].deliveryTime =  hashMap.lookUp(truck1.packages[i])[1].deliveryTime + timedelta(hours = 8)
        i = i + 1


    #Truck 2, leaves at 9:05AM
    i = 0
    while(i < len(truck2.packages)):
        hashMap.lookUp(truck2.packages[i])[1].deliveryTime =  hashMap.lookUp(truck2.packages[i])[1].deliveryTime + timedelta(hours = 9, minutes = 5)
        i = i + 1


    #Truck 3, leaves atfter truck 1 returns
    i = 0
    while(i < len(truck3.packages)):
        #Each packages delivery travel time + Truck 3's return to hub time
        hashMap.lookUp(truck3.packages[i])[1].deliveryTime =  hashMap.lookUp(truck3.packages[i])[1].deliveryTime + timedelta(hours = 8, minutes = (truck1.mileage / 0.3))

        i = i + 1









#Returns delivery status for a single package based on a given time. compare given time to its delivery time.
def deliveryStatus(givenTime, hashMap, packageId):

    #turns the user given time in format XX:XX (Hour:minute) into hour and minute variables
    hour = (int(givenTime[0]) * 10) + int(givenTime[1])
    minute = (int(givenTime[3]) * 10) + int(givenTime[4])


    if(hashMap.lookUp(packageId)[1].deliveryTime > timedelta(hours = hour, minutes = minute)):

        return "   is Out for Delivery"
    else:
        return " was Delivered at: ", str(hashMap.lookUp(packageId)[1].deliveryTime).split(".")[0]









#Print out to console the status of every package at a given specific time.
def deliveryList(givenTime, hashMap):
    i = 0

    while(i < hashMap.size):
        if(hashMap.map[i]):
            print("Package ID:", hashMap.map[i][1].packageID, deliveryStatus(givenTime, hashMap, hashMap.map[i][1].packageID))
        i = i + 1




#Prints truck info and stats, then wait for user input. Print out the info using DeliveryList
def userInterface(hashMap, truck1, truck2, truck3):

    miles = truck1.mileage + truck2.mileage + truck3.mileage


    print("Total miles driven by all trucks: ", miles)
    print("")
    print("Truck 1 has the packages: ", truck1.packages)
    print("Truck 1's sorted delivery path is: ", truck1.route)
    print("")
    print("Truck 2 has the packages: ", truck2.packages)
    print("Truck 2's sorted delivery path is: ", truck2.route)
    print("")
    print("Truck 3 has the packages: ", truck3.packages)
    print("Truck 3's sorted delivery path is: ", truck3.route)
    print("")


    while(True):
        givenTime = input("Enter a time in the format XX:XX (Hour:minute, 08:45 or 14:30) to check package status or EXIT to close program \n")

        if(givenTime.__contains__("EXIT")):
            break

        deliveryList(givenTime, hashMap)