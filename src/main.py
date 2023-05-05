import funcs
import constants
import numpy as np


chroms = funcs.generate_chroms(constants.NUM_OF_CHROMS, constants.NUM_GEN_RANGE)


chroms_evals = list(map(lambda chrom: funcs.eval(chrom), chroms))
chroms_fitness = list(map(lambda eval: 1 / eval, chroms_evals))
total_fitness = sum(chroms_fitness)
chroms_probs = list(map(lambda fitness: fitness / total_fitness, chroms_fitness))
cum_probs = np.cumsum(chroms_probs)

new_chroms = [None] * len(chroms)

# get new generation with roulette selection
for i in range(len(chroms)):
    rand = np.random.uniform(0, cum_probs[-1])
    new_chroms[i] = chroms[funcs.get_roulette_position(rand, cum_probs)]
