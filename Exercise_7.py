'''
Use the Vehicle class of the previous exercise (6). Add the following methods to the class:

- a method that takes as argument a tuple of two numbers and updates the velocity of the car to the input argument.
- a method that prints all the attributes of the car
- a method called "emissions". This method takes as argument a number (the distance travelled) and returns
  the amount of emissions produced by the Vehicle for that distance. If the vehicle is a non electric car
  the method will return 10 * distance, if the vehicle is a non electric truck, the  method will return 50 * distance. 
  If the vehicle is an electric car, the method will return 1 * distance and if the vehicle is an electric truck,
  the method will return 5 * distance. 

Weight: 2
'''

from numpy import array

class Vehicle:

    def __init__(self, type, velocity, color, electric):
        self.type = type
        self.velocity = velocity
        self.color = color
        self.electric = electric

    def changeVel(self, vel):
        self.velocity = array(vel)

    def display(self):

        print("Vehicle Attributes")
        print("-"*16)
        print("-"*16)
        print(f"Type of vehicle: {self.type}")
        print(f"Velocity of vehicle: {self.velocity}")
        print(f"Color of vehicle: {self.color}")
        print(f"Electric vehicle: {self.electric}")
        print("-"*16)
        print("-"*16)

    def emissions(self, distance):

        emission = 0

        if self.type == "Car" and self.electric:
          emission = 1 * distance
        elif self.type == "Car" and not(self.electric):
          emission = 10 * distance

        elif self.type == "Truck" and self.electric:
          emission = 5 * distance
        elif self.type == "Truck" and not(self.electric):
          emission = 50 * distance

        return emission
