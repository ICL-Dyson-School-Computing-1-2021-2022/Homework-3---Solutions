'''
Write a class Vehicle, that takes in (via the constructor) the following attributes:

- type of the Vehicle (a string that can be either "Car" or "Truck")
- the velocity of the Vehicle (a tuple with two numbers, x and y)
- the color of the vehicle (a string)
- wheter or not the vehicle is electric (a boolean, True if it is an electric vehicle, False otherwise)

In the constructor argument, transform the tuple that you get as an input into a Numpy array.

Weight: 1
'''
from numpy import array

class Vehicle:
    def __init__(self, type, velocity, color, electric):
        self.type = type
        self.velocity = array(velocity)
        self.color = color
        self.electric = electric