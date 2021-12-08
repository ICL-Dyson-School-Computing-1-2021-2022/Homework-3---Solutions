import numpy as np
import time


list1 = []
list2 = []
for i in range(10000000):
    list1.append(i)
    list2.append(2*i)
start_time = time.time()
listsqr = [i**2 for i in list1]
print("--- %s seconds ---" % (time.time() - start_time))

array = np.array(list1)
start_time = time.time()
arraysqr = np.power(array,2)
print("--- %s seconds ---" % (time.time() - start_time))