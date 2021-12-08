'''
Using the vehicle class that you created in the previous exercises, create 200 objects vehicle.
50 of them will be electric cars, 50 of them will be non electric cars. 50 of them will be electric trucks and
50 of them will be non electric trucks. The attribute velocity will be initialised randomly (with a positive number).

Write a function that takes as arguments a list of vehicles and a positive real number t (that represents time). The function will output the average 
emission for each category of vehicles (so, 4 averages, electric and non electric cars and trucks).

Notice that the velocity of each vehicle is expressed in terms of x and y component and you need to compute the total distance travelled.

hint: divide this exercise in subproblems and write appropriate functions for each subproblem

Weight: 3
'''

import Exercise_7 as ex
import numpy as np


def distance(t, velocity):
    
    speed = np.linalg.norm(velocity)  # norm of the vector
    dist = speed*t

    return dist

def mean(inputList):

    if len(inputList) > 0: 
        

        return sum(inputList)/len(inputList)

    else:
        # you also need to take into account that there could be 
        # no vehicle of that category in the list

        return 0



def computeEmissions(vehicle, t):

    dist = distance(t, vehicle.velocity)
    return vehicle.emissions(dist)



def averages(vehicles, t, verbose = False):
    '''Computes the average emissions for each vehicle type'''

    emissionsEV = []
    emissionsET = []
    emissionsICV = []
    emissionsICT = []

    for vehicle in vehicles:
        
        if vehicle.type == "Car" and vehicle.electric:
            
            # Emissions for EVs
            emissionsEV.append(computeEmissions(vehicle, t))

        elif vehicle.type == "Truck" and vehicle.electric:

            # Emissions for ETs
            emissionsET.append(computeEmissions(vehicle, t))

        elif vehicle.type == "Car" and not(vehicle.electric):

            # Emissions for ICVs
            emissionsICV.append(computeEmissions(vehicle, t))

        elif vehicle.type == "Truck" and not(vehicle.electric):
            
            # Emissions for ICTs
            emissionsICT.append(computeEmissions(vehicle, t))


    averageEV = mean(emissionsEV)
    averageET = mean(emissionsET)
    averageICV = mean(emissionsICV)
    averageICT = mean(emissionsICT)

    if verbose:

        # Print the results

        print(f" Average emissions for EV: {averageEV}")
        print(f" Average emissions for ET: {averageET}")
        print(f" Average emissions for ICV: {averageICV}")
        print(f" Average emissions for ICT: {averageICT}")

    return (averageEV, averageET, averageICV, averageICT)



N = 50
time = 20
maxVelocity = 100
electric = True

vehicles = []


for i in range(N):  # Create N Electric cars
    velocity = (np.random.random() * maxVelocity, np.random.random() * maxVelocity)
    vehicles.append(ex.Vehicle("Car", velocity, "Blue", electric))
    
for i in range(N):  # Create N Electric trucks
    velocity = (np.random.random() * maxVelocity, np.random.random() * maxVelocity)
    vehicles.append(ex.Vehicle("Truck", velocity, "Blue", electric))

for i in range(N):  # Create N Internal combutions vehicles
    velocity = (np.random.random() * maxVelocity, np.random.random() * maxVelocity)
    vehicles.append(ex.Vehicle("Car", velocity, "Blue", not(electric)))

for i in range(N):  # Create N Internal combutions trucks
    velocity = (np.random.random() * maxVelocity, np.random.random() * maxVelocity)
    vehicles.append(ex.Vehicle("Truck", velocity, "Blue", not(electric)))



averages(vehicles, time, verbose = True)