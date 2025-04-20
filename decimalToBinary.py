import numpy as np
arr = np.array

def decToBinaryForNpArray(arr):
    binStr = ""
    for val in arr:
        binStr += str(bin(val))