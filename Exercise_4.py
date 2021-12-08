'''
In this folder you will find a subfolder with a file "Data points.txt".
- The first column of the text file provides a list of 1000 points related to sensor 1
- The second column of the text file provides a list of 1000 points related to sensor 2

Write a program that extracts data from the file and computes the average 
of the two measurements (for each row, the average between sensor 1 and sensor 2). 
You will end up with 1000 data points that you need to write in another text file called "Data points average.txt"

Weight: 2
'''

import os

os.chdir("Data")

with open("Data points.txt", "r") as file:
    textData = file.read()

listData = textData.split()
data1 = []
data2 = []
for i in range(2,len(listData),2): # Skip the first two lines
    data1.append(float(listData[i]))
    data2.append(float(listData[i+1]))

avgData = [(i+j)/2 for i,j in zip(data1, data2)]

with open("Data points average.txt", "w") as file:
    file.write("-"*16 + "\n")
    file.write("-"*16 + "\n")
    for dataPoint in avgData:
        file.write(f"{dataPoint}\n")