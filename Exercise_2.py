'''
Write a program to create a Numpy vector with values ranging 
from 15 to 55 and print all values except the first one and the last one.

Weight: 1
'''
import numpy as np

array = np.arange(15,56)

print(array[1:-1])
