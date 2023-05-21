from dataclasses import fields
from models import Chromosome
from typing import Final

# GA params
NUM_GEN_RANGE: Final = [-10, 10]
NUM_OF_CHROMS: Final = 50
GENERATIONS: Final = 100
MUTATION_RATE: Final = 0.3
MUTATION_VALUE_CHANGE: Final = 0.01
CROSSOVER_RATE: Final = 0.2

# for tournament selection
NUM_OF_CONTESTANTS = 10

# for evaluation
ITERATIONS = 100
SOLUTION = 0

# generic helper constants
NUM_OF_GENES: Final = len(list(fields(Chromosome)))
CHROM_FIELDS_NAMES: Final = list(map(lambda field: field.name, fields(Chromosome)))