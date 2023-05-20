from matplotlib import pyplot as plt 
import numpy as np
import funcs
import constants


CHROMS = funcs.generate_chroms(constants.NUM_OF_CHROMS, constants.NUM_OF_GENES, constants.NUM_GEN_RANGE)
BEST_EVALS_OVER_GENS = [funcs.get_best_eval(CHROMS)]


for gen in range(constants.ITERATIONS):
    chroms_evals = list(map(lambda chrom: funcs.eval(chrom), CHROMS))
    chroms_fitness = list(map(lambda eval: 1 / eval, chroms_evals))
    total_fitness = sum(chroms_fitness)
    chroms_probs = list(map(lambda fitness: fitness / total_fitness, chroms_fitness))
    cum_probs = np.cumsum(chroms_probs)


    # get new generation with roulette selection
    new_chroms = [None] * constants.NUM_OF_CHROMS

    for i in range(constants.NUM_OF_CHROMS):
        rand = np.random.uniform(0, cum_probs[-1])
        new_chroms[i] = CHROMS[funcs.get_roulette_position(rand, cum_probs)]


    # parents selection
    parent_indexes = []

    for i in range(constants.NUM_OF_CHROMS):
        if (np.random.uniform(0, 1) < constants.CROSSOVER_RATE):
            parent_indexes.append(i)


    # crossover if more parents than 1
    if len(parent_indexes) >= 1:
        for index in range(len(parent_indexes)):
            next_index = index + 1 if index != len(parent_indexes) - 1 else 0
            parent1_index = parent_indexes[index]
            parent2_index = parent_indexes[next_index]
            new_chroms[parent1_index] = funcs.perform_crossover(new_chroms[parent1_index], new_chroms[parent2_index])


    # mutation
    num_of_genes_to_change = int(constants.MUTATION_RATE * constants.NUM_OF_CHROMS * constants.NUM_OF_GENES)
    genes_to_change_positions = [None] * num_of_genes_to_change

    for index in range(num_of_genes_to_change):
        chrom_index = np.random.randint(0, constants.NUM_OF_CHROMS)
        gene_index = np.random.randint(0, constants.NUM_OF_GENES)
        genes_to_change_positions[index] = (chrom_index, gene_index)

    funcs.perform_mutation(genes_to_change_positions, new_chroms)


    # store generation data
    CHROMS = new_chroms
    BEST_EVALS_OVER_GENS.append(funcs.get_best_eval(CHROMS))


# plot results
x = np.arange(0, constants.ITERATIONS + 1) 
y = BEST_EVALS_OVER_GENS 
plt.title("Best Values Over Generations") 
plt.xlabel("Generation") 
plt.ylabel("Best Value") 
plt.plot(x, y) 
plt.show()
