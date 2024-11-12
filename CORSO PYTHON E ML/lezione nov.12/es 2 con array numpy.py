import numpy as np
import random

arr1=np.random.randint(1,20,(4,4))
print("Array 1 : \n ",arr1)

arr2=np.random.randint(11,28,(4,4))
print("Array 2 : \n ",arr2)


arr1somma=np.sum(arr1[-1][1:])
print("Somma su array1 ", arr1somma)

arr2somma=np.sum(arr2[-1][1:])
print("Somma su array2 ", arr2somma)

arr3= np.concatenate((arr1,arr2),axis=1)
print(arr3)