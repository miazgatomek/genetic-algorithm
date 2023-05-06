from dataclasses import fields
from models import Chromosome

NUM_GEN_RANGE = [-30, 30]
NUM_OF_CHROMS = 100
ITERATIONS = 100
MUTATION_RATE = 0.3
MUTATION_VALUE_CHANGE = 0.01
CROSSOVER_RATE = 0.2
NUM_OF_GENES = len(list(fields(Chromosome)))
CHROM_FIELDS_NAMES = list(map(lambda field: field.name, fields(Chromosome)))