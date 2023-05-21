from matplotlib import pyplot as plt 
import numpy as np
import funcs
import constants
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--selection')
selection_type = parser.parse_args().selection
selection_type = 'roulette' if selection_type is None else selection_type


CHROMS = funcs.generate_chroms(constants.NUM_OF_CHROMS, constants.NUM_OF_GENES, constants.NUM_GEN_RANGE)
BEST_EVALS_OVER_GENS = [funcs.get_best_eval(CHROMS)]


for gen in range(constants.ITERATIONS):
    chroms_evals = list(map(lambda chrom: funcs.eval(chrom), CHROMS))
    chroms_fitness = list(map(lambda eval: 1 / eval, chroms_evals))
    total_fitness = sum(chroms_fitness)
    chroms_probs = list(map(lambda fitness: fitness / total_fitness, chroms_fitness))
    cum_probs = np.cumsum(chroms_probs)


    # get new generation with specified selection method
    new_chroms = [None] * constants.NUM_OF_CHROMS

    match selection_type:
        case 'roulette':
            for i in range(constants.NUM_OF_CHROMS):
                rand = np.random.uniform(0, cum_probs[-1])
                new_chroms[i] = CHROMS[funcs.get_roulette_position(rand, cum_probs)]

        case 'tournament':
            for i in range(constants.NUM_OF_CHROMS):
                contestant_indexes = np.random.randint(constants.NUM_OF_CHROMS, size=constants.NUM_OF_CONTESTANTS)
                contestant_evals = list(map(lambda index: funcs.eval(CHROMS[index]), contestant_indexes))
                winner_index = contestant_indexes[contestant_evals.index(min(contestant_evals))]
                new_chroms[i] = CHROMS[winner_index]


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


# indicate best chromosome
best_chrom = CHROMS[funcs.get_best_eval_position(CHROMS)]
print(best_chrom, funcs.eval(best_chrom))


# plot results
x = np.arange(0, constants.ITERATIONS + 1)
y = BEST_EVALS_OVER_GENS
plt.title("Best Values Over Generations")
plt.xlabel("Generation")
plt.ylabel("Best Value")
plt.plot(x, y)
plt.show()
