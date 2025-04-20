import numpy as np
import genvars as gv

def geneticAlgorithm(population_size, max_iterations,):
    gv.size_of_population = population_size
    initial_random_population = gv.initial_random_population
    population = initial_random_population
    for i in range(max_iterations):
        dec