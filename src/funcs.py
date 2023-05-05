from models import Chromosome
from dataclasses import fields
import numpy as np

def fitness(c: Chromosome):
    return pow(c.x, 2) + pow(c.y, 2)

def generate_chroms(num_of_chroms: int, range: list[float]):
    chrom_class_param_count = len(list(fields(Chromosome)))
    lambda_map_to_chroms = lambda arr: Chromosome(*arr)
    return list(map(lambda_map_to_chroms, np.random.uniform(range[0], range[1], [num_of_chroms, chrom_class_param_count])))
