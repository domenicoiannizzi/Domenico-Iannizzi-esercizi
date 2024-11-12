import numpy as np
import random
from scipy import stats


arr1= np.random.randint(1,1000,50)
print("Array 1",arr1)

moda=stats.mode(arr1)
print(moda)

media=np.mean(arr1)
print("Media :",media)

dev=np.std(arr1)
print("deviazione standard: ", dev)

x=arr1.reshape(5,10)
print(x)