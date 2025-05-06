import numpy as np
import genvars as gv
import random as random
import decimalToBinary as dtb

def geneticAlgorithm(population_size, max_iterations):

    size_of_population = population_size
    initial_random_population = gv.generateInitialRandomPopulation(size_of_population)
    population = initial_random_population

    print("The initial population is:\n")
    print(population,"\n")
    print("==================================================================\n")

    for i in range(max_iterations):
        binStr = dtb.decToBinaryForNpArray(population)


        if gv.type_of_crossover == "single_point_crossover": #crossover
            parent1, parent2 = random.sample(range(len(binStr)), 2)
            crossover_point = random.randint(1,len(binStr[0]))
            print("crossover point:", {crossover_point})

            binStr_parent1 = list(binStr[parent1])
            binStr_parent2 = list(binStr[parent2])

            for k in range (crossover_point,len(binStr[0])): #single point crossover
                t = binStr_parent1[k]
                binStr_parent1[k] = binStr_parent2[k]
                binStr_parent2[k] = t
            
            binStr[parent1] = "".join(binStr_parent1)
            binStr[parent2] = "".join(binStr_parent2)

        if gv.type_of_mutation == "single_point_mutation": #mutation
            parent = random.randint(0,len(binStr) - 1)
            mutation_point = random.randint(0,len(binStr[0]) - 1)
            parent ^= ( 1 << (len(binStr[0]) - mutation_point - 1) )  #single point mutation    
        #converting the binary number back to decimal

        population = dtb.binToDecimal(binStr)

        population = np.clip(population,min=10,max = 99,dtype=int)

        print(population,"\n")
        print("==================================================================\n")

geneticAlgorithm(3,4)