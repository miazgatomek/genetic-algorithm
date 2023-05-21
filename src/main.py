from matplotlib import pyplot as plt 
import numpy as np
import funcs
import constants
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--selection', default='roulette')
parser.add_argument('-d', '--debug', default=False)
args = parser.parse_args()
selection_type = args.selection
debug = args.debug


def genetic_algorithm(show_plot=False):
    chroms = funcs.generate_chroms(constants.NUM_OF_CHROMS, constants.NUM_OF_GENES, constants.NUM_GEN_RANGE)
    best_evals_over_gens = [funcs.get_best_eval(chroms)]

    for gen in range(constants.GENERATIONS - 1):
        chroms_evals = list(map(lambda chrom: funcs.eval(chrom), chroms))
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
                    new_chroms[i] = chroms[funcs.get_roulette_position(rand, cum_probs)]

            case 'tournament':
                for i in range(constants.NUM_OF_CHROMS):
                    contestant_indexes = np.random.randint(constants.NUM_OF_CHROMS, size=constants.NUM_OF_CONTESTANTS)
                    contestant_evals = list(map(lambda index: funcs.eval(chroms[index]), contestant_indexes))
                    winner_index = contestant_indexes[contestant_evals.index(min(contestant_evals))]
                    new_chroms[i] = chroms[winner_index]


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
        chroms = new_chroms
        best_evals_over_gens.append(funcs.get_best_eval(chroms))


    # indicate best chromosome
    best_chrom = chroms[funcs.get_best_eval_position(chroms)]
    print(best_chrom, funcs.eval(best_chrom))


    # plot results
    if show_plot:
        x = np.arange(0, constants.GENERATIONS + 1)
        y = best_evals_over_gens
        plt.title('Best Values Over Generations')
        plt.xlabel('Generation')
        plt.ylabel('Best Value')
        plt.plot(x, y)
        plt.show()

    return best_chrom


if debug:
    genetic_algorithm(True)
else:
    best_chroms = []

    for i in range(constants.ITERATIONS):
        best_chroms.append(genetic_algorithm())
        print(i)

    best_chroms_errors = list(map(lambda chrom: funcs.eval(chrom) - constants.SOLUTION, best_chroms))
    average_error = sum(best_chroms_errors) / len(best_chroms_errors)

    x = np.arange(1, constants.ITERATIONS + 1)
    y = best_chroms_errors
    plt.title('GA errors; selection = %s ; average = %s' % (selection_type, average_error))
    plt.xlabel('Run')
    plt.ylabel('Error')
    plt.yscale('log')
    plt.plot(x, y)
    plt.show()
    