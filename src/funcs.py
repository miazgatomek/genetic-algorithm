from common import Chromosome
import numpy as np

def fitness(c: Chromosome):
    return pow(c.x, 2) + pow(c.y, 2)

def generate_chroms(num_of_chroms: int, range: list[float]):
    lambda_map_to_chroms = lambda arr: Chromosome(arr[0], arr[1])
    return list(map(lambda_map_to_chroms, np.random.uniform(range[0], range[1], [num_of_chroms, 2])))
