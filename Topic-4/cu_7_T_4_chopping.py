"""What Is An Index : Index Is Nothing But Accessing Values Or Elements Of An Array
Like : arr=np.array([1,2,3,4,5])
print(arr[0]) means we tells to the python interpreter to access the first element of an corresponding array.
indexing: 0->1st element 
         1->2nd element
         -1->first last element
         -2 -> second last element"""

import numpy as np

def slicing():
    arr=np.array([1,2,3,4,5])
    print("------Using The Slicing ------ ")
    print(arr[0],end="\n")
    print(arr[1],end="\n")
    print(arr[1:5],end="\n")
    print(arr[-1],end="\n")
    print(arr[-2],end="\n")
    print(arr[:2],end="\n")
    print(arr[2:],end="\n")
    print(arr[:-2],end="\n")

slicing()
"""Boolean Masking : Used For data Filteration"""

def bool_mask():
    arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    """My Requirement is to print all the even numbers in the respective array"""
    print(arr[arr %2==0],end=" ")

bool_mask()
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

# Create Boolean Mask
prime_array = np.array([is_prime(a) for a in arr])

print("Prime Numbers:")
print(arr[prime_array])