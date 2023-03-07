# PackageDelivery
 WGU C950 project. Mail delivery simulation. Given package list, package delivery requirements, and city data



I worked on a traveling salesman problem by developing a mail delivery simulation project. The project involved developing an algorithm and writing code to optimize the delivery of 40 packages in Salt Lake City, Utah, using three trucks and two drivers. The program ensured that all packages were delivered on time while meeting specific delivery requirements, and the combined total distance traveled was kept under 140 miles for both trucks. I also implemented a real-time tracking feature to monitor the progress of each truck and package. The program allowed supervisors to check the status of each package delivery, including whether it had been delivered and at what time. Additionally, the program enabled users to enter any time of the day to see which packages had already been delivered and which ones were still pending. This project helped me improve my problem-solving skills and algorithmic thinking.


![Program running with delivery status](https://i.imgur.com/B0xCk80.png "Program running with delivery status")


### ASSUMPTIONS

•   Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.

•   The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.

•   There are no collisions.

•   Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.

•   Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 

•   The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).

•   There is up to one special note associated with a package.

•   The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 am. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.

•   The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.

•   The day ends when all 40 packages have been delivered.
