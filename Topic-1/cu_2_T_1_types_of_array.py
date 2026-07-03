"""The Array Is Different Types Like realnumbers , Zero , all-ones matrix"""
import numpy as np
if __name__=="__main__":
    real_number_array=np.array([1,2,3,4])
    print(real_number_array,end=" ")
    print("\n")
    try:

        zero_array=np.zeros((2 , 3))
        print(zero_array)
        print("\n")
    except TypeError:
        print("You Are Missing ()  😢")
    
    try :
        all_ones_array=np.ones((2,4))
        print(all_ones_array)

    except TypeError:
        print("It Is A Touole And You Are Missing ()")

"""Explanation"""
"""As We Know Mainly The Arrays Are Three Types 
1.np.array([elements1,elements2,......elements(n)])where n=1,2,3,4,5.....
2.np.zeroes((row_number,column_number)).The shape dimensions must be passed together as a tuple like....
3.np.ones((row,column))The shape dimensions must be passed together as a tuple like...."""
