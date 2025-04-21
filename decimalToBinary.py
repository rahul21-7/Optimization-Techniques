import numpy as np
arr = np.array()

def decToBinaryForNpArray(arr):
    binStr = [bin(val)[2:] for val in arr]
    return np.array(binStr,dtype=str)