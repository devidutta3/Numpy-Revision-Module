#Numpy Performs Operations on All Elements automatically

import numpy as np

def addition(array_1,array_2):
    array_sum=np.add(array_1,array_2)
    array_sub=np.subtract(array_1,array_2)
    array_multi=np.multiply(array_1,array_2)
    array_div=np.divide(array_1,array_2)
    return array_sum , array_sub , array_multi , array_div


try:
    array_1=np.array([1,11])
    array_2=np.array([1,15])
    result=addition(array_1,array_2)
    print(result,end="\n")
except TypeError:
    print("Try Again.....")