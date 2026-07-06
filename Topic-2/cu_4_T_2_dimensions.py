"""we know according to the dimensions it is of 3 types 
1. 1D array
2.2D array -> Syntax [[elements1,elements2,......elements(n)],
                      [[elements1,elements2,......elements(n)]]
3.3D array 
ndim used to check what is dimension of respective array"""

import numpy as np
if __name__=="__main__":
    try:

        one_di=np.array([1,2,3,4])
        two_di=np.array([[1,2,3],
                        [4,5,6]])
        three_di=np.array([
    [[1, 2, 3], [4, 5, 6]],  # Layer 0
    [[7, 8, 9], [10, 11, 12]] # Layer 1
])
        print(one_di.ndim)
        print(two_di.ndim)
        print(three_di.ndim)

    except TypeError:
        print("Try Again.....")
"""The 3D array is created by layers ,row,column
"""