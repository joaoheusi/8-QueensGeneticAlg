import numpy as np
import ga
equation_inputs = [4,-2,3.5,5,-11,-4.7]
num_weights = 6

sol_per_pop = 8

pop_size = (sol_per_pop,num_weights)

new_population = np.random.uniform(low=-4.0, high=4.0, size= pop_size)

#print(new_population)

num_generetion = 5
num_parents_mating = 4

for generation in range(num_generetion):
    fitness = ga.chromosomes.

