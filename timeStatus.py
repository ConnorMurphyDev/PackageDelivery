from hashMap import HashMap
from datetime import datetime, timedelta



#deliveredAt function. Set a delivery time for each package. use some sort of time variable so they're easy to compare
#Alter the decideroute function to keep the total miles at point of delivery. calculate delivery time based of the miles
def deliveredAt(hashMap, truck1, truck2, truck3):

    i = 0
    while(i < hashMap.size):

        if(hashMap.map[i]):
            #Without the departure time added yet, we are adding minutes to the delivery time based on the miles traveled on delivery, since the truck moves at 18MPH
            hashMap.map[i][1].deliveryTime = timedelta(minutes = (18 / hashMap.map[i][1].deliveryMiles * 60))
            i = i + 1



    #Adjusting delivery times for the departure of truck 1, leaves at 8AM
    i = 0
    while(i < len(truck1.packages)):
        hashMap.lookUp(truck1.packages[i])[1].deliveryTime =  hashMap.lookUp(truck1.packages[i])[1].deliveryTime + timedelta(hours = 8)
        i = i + 1


    #Adjusting delivery times for the departure of truck 2, leaves at 9:05AM
    i = 0
    while(i < len(truck2.packages)):
        hashMap.lookUp(truck2.packages[i])[1].deliveryTime =  hashMap.lookUp(truck2.packages[i])[1].deliveryTime + timedelta(hours = 9, minutes = 5)
        i = i + 1


    #Adjusting delivery times for the departure of truck 3, leaves atfter truck 1 returns
    #truck 1 return time will be defined as truck 1's final delivery miles converted to minutes plus its departure time
    i = 0
    while(i < len(truck3.packages)):
        hashMap.lookUp(truck3.packages[i])[1].deliveryTime =  hashMap.lookUp(truck3.packages[i])[1].deliveryTime + timedelta(hours = 8, minutes = (18 / hashMap.map[i][1].deliveryMiles * 60))
        i = i + 1









#deliveryStatus. Returns at hub, en route, or delivered for a single package based on a given time. compare given time to
# its delivery time. Give each truck a leave time for at hub. Recieves a string in format XX:XX (Hour:minute)
def deliveryStatus(givenTime, hashMap, packageId):

    #turns the user given time in format XX:XX (Hour:minute) into hour and minute variables
    hour = (int(givenTime[0]) * 10) + int(givenTime[1])
    minute = (int(givenTime[3]) * 10) + int(givenTime[4])

    #if(hashMap.lookUp(packageId)[1].deliveryTime > datetime(year = 0, month = 0, day = 0, hour = hours, minute = minutes)):
    if(hashMap.lookUp(packageId)[1].deliveryTime > timedelta(hours = hour, minutes = minute)):

        return "   is Out for Delivery"
    else:
        return " was Delivered at: ", str(hashMap.lookUp(packageId)[1].deliveryTime).split(".")[0]









#DeliveryList. Print out to console the status of every package at a given specific time. use delivery status
def deliveryList(givenTime, hashMap):
    i = 0

    while(i < hashMap.size):
        if(hashMap.map[i]):
            print("Package ID:", hashMap.map[i][1].packageID, deliveryStatus(givenTime, hashMap, hashMap.map[i][1].packageID))
        i = i + 1




#UserInterface. print out each trucks load, its delivery route, miles driven for each truck, total miles
#Print out asking for a time to check the status for. Then wait for user input. Print out the info using DeliveryList
#then loop and wait for another input
def userInterface(hashMap, truck1, truck2, truck3):

    miles = truck1.mileage + truck2.mileage + truck3.mileage

    print("Last delivery made at:            ", str(hashMap.lookUp(truck3.route[-1])[1].deliveryTime).split(".")[0])
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