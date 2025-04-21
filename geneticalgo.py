import numpy as np
import genvars as gv
import random as random
import decimalToBinary as dtb

def geneticAlgorithm(population_size, max_iterations,):
    gv.size_of_population = population_size
    initial_random_population = gv.initial_random_population
    population = initial_random_population
    for i in range(max_iterations):
        binStr = dtb.decToBinaryForNpArray(population)
        if gv.type_of_crossover == "single_point_crossover":
            parent1, parent2 = random.sample(range(len(binStr)), 2)
            crossover_point = random.randint(1,len(binStr[0]))
            for k in range (crossover_point,len): #single point crossover
                t = binStr(parent1)[k]
                binStr(parent1)[k] = binStr(parent2)[k]
                binStr(parent2)[k] = t