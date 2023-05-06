from models import Chromosome
from dataclasses import fields
import constants
import numpy as np


def eval(chrom: Chromosome):
    # return pow(chrom.x, 2) + pow(chrom.y, 2) + pow(chrom.z, 2)
    return pow(chrom.x, 2) + pow(chrom.y, 2)


def get_best_eval(chroms: list[Chromosome]):
    return min(list(map(lambda chrom: eval(chrom), chroms)))


def generate_chroms(num_of_chroms: int, range: list[float]):
    lambda_map_to_chroms = lambda arr: Chromosome(*arr)
    field_values = np.random.uniform(range[0], range[1], [num_of_chroms, constants.NUM_OF_GENES])

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
        #optional enhancement by selecting which fits better
        new_value += constants.MUTATION_VALUE_CHANGE if bool(np.random.choice([True, False])) else (-constants.MUTATION_VALUE_CHANGE)
        setattr(chroms[positions[0]], constants.CHROM_FIELDS_NAMES[positions[1]], new_value)
