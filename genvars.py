import numpy as np
import pandas as pd
import random as random

size_of_population = random.randint(10,1000)


type_of_crossover = "single_point_crossover"
type_of_mutation = "single_point_mutation"

def generateInitialRandomPopulation(size_of_population):
    return np.random.randint(low=10,high=99,size=size_of_population)





# print((initial_random_population*10).astype(int))


