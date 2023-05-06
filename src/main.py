import funcs
import constants
import numpy as np


chroms = funcs.generate_chroms(constants.NUM_OF_CHROMS, constants.NUM_GEN_RANGE)
chroms_evals = list(map(lambda chrom: funcs.eval(chrom), chroms))
chroms_fitness = list(map(lambda eval: 1 / eval, chroms_evals))
total_fitness = sum(chroms_fitness)
chroms_probs = list(map(lambda fitness: fitness / total_fitness, chroms_fitness))
cum_probs = np.cumsum(chroms_probs)


# get new generation with roulette selection
new_chroms = [None] * len(chroms)

for i in range(len(chroms)):
    rand = np.random.uniform(0, cum_probs[-1])
    new_chroms[i] = chroms[funcs.get_roulette_position(rand, cum_probs)]


# parents selection
parent_indexes = []

for i in range(len(new_chroms)):
    if (np.random.uniform(0, 1) < constants.CROSSOVER_RATE):
        parent_indexes.append(i)


# crossover if more parents than 1
if len(parent_indexes) >= 1:
    for index in range(len(parent_indexes)):
        next_index = index + 1 if index != len(parent_indexes) - 1 else 0
        parent1_index = parent_indexes[index]
        parent2_index = parent_indexes[next_index]
        new_chroms[parent1_index] = funcs.crossover(new_chroms[parent1_index], new_chroms[parent2_index])


# mutation