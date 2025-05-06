import numpy as np
arr = np.array([1,2,3])

def decToBinaryForNpArray(arr):
    binStr = [bin(int(val))[2:] for val in arr]
    return np.array(binStr,dtype=str)

def binToDecimal(arr):
    decStr = [int(val, 2) for val in arr]
    return np.array(decStr,dtype = int)