from dataclasses import dataclass

@dataclass
class Chromosome:
    x: float
    y: float

NUM_GEN_RANGE = [-100, 100]
NUM_OF_CHROMS = 100
MUTATION_PROB = 1
