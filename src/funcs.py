from models import Chromosome
import numpy as np
import constants


def eval(chrom: Chromosome):
    # Booth's function - search in range [-10, 10]
    # f(1, 3) = 0
    return pow((chrom.x + 2 * chrom.y - 7), 2) + pow((2 * chrom.x + chrom.y - 5), 2)


def get_best_eval(chroms: list[Chromosome]):
    return min(list(map(lambda chrom: eval(chrom), chroms)))


def get_best_eval_position(chroms: list[Chromosome]):
    best_eval = get_best_eval(chroms)
    return list(map(lambda chrom: eval(chrom), chroms)).index(best_eval)


def generate_chroms(num_of_chroms: int, num_of_genes: int, range: list[float]):
    lambda_map_to_chroms = lambda arr: Chromosome(*arr)
    field_values = np.random.uniform(range[0], range[1], [num_of_chroms, num_of_genes])

    return list(map(lambda_map_to_chroms, field_values))


def get_roulette_position(rand, cum_probs: list[float]):
    for i in range(len(cum_probs)):
        if i == 0 and rand <= cum_probs[0]:
            return 0
        elif rand > cum_probs[i] and rand <= cum_probs[i + 1]:
            return i + 1


def perform_crossover(parent1: Chromosome, parent2: Chromosome):
    max_cut_off_index = constants.NUM_OF_GENES - 1
    cut_off_index = np.random.randint(0, max_cut_off_index)
    new_attributes = [None] * constants.NUM_OF_GENES

    for i in range(constants.NUM_OF_GENES):
        parent = parent1 if i <= cut_off_index else parent2
        new_attributes[i] = getattr(parent, constants.CHROM_FIELDS_NAMES[i])

    return Chromosome(*new_attributes)


def perform_mutation(genes_to_change_positions: list[tuple], chroms: list[Chromosome]):
    for positions in genes_to_change_positions:
        new_value = getattr(chroms[positions[0]], constants.CHROM_FIELDS_NAMES[positions[1]])
        # optional enhancement by selecting which fits better
        new_value += constants.MUTATION_VALUE_CHANGE if bool(np.random.choice([True, False])) else (-constants.MUTATION_VALUE_CHANGE)
        setattr(chroms[positions[0]], constants.CHROM_FIELDS_NAMES[positions[1]], new_value)
