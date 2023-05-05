from dataclasses import dataclass
from random import uniform
from typing import List
import numpy as np

@dataclass
class Chromosome:
    x: float
    y: float

mutation_prob = 1
value_gen_range = [-100, 100]

def fitness(c: Chromosome):
    return pow(c.x, 2) + pow(c.y, 2)

def generate_chroms(num_of_chroms: int, range: List[float]):
    lambda_map_to_chroms = lambda arr: Chromosome(arr[0], arr[1])
    return list(map(lambda_map_to_chroms, np.random.rand(num_of_chroms, 2)))

print(generate_chroms(10, value_gen_range))

