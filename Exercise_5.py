'''
In this folder you will find a subfolder with a file "Data points.txt".
- The first column of the text file provides a list of 1000 points related to sensor 1
- The second column of the text file provides a list of 1000 points related to sensor 2

Write a program that extracts data from the file and plot them using matplotlib.pyplot.
The data relative to both sensors need to be plotted in the same graph (they are both relative to the y axis),
using different colors.
Add the following label to the x axis: "Time [s]"
Add the following label to the y axis: "Force [N]"

Weight: 2
'''


import os
import matplotlib.pyplot as plt
os.chdir("Data")

with open("Data points.txt", "r") as file:
    textData = file.read()

listData = textData.split()
data1 = []
data2 = []
for i in range(2,len(listData),2):
    data1.append(float(listData[i]))
    data2.append(float(listData[i+1]))

plt.plot(data1)
plt.plot(data2)
plt.xlabel("Time [s]")
plt.ylabel("Force [N]")
plt.show()