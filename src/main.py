import funcs
import constants

chroms = funcs.generate_chroms(constants.NUM_OF_CHROMS, constants.NUM_GEN_RANGE)
chroms_evals = list(map(lambda chrom: funcs.eval(chrom), chroms))
chroms_fitness = list(map(lambda eval: 1 / eval, chroms_evals))
total_fitness = sum(chroms_fitness)
chroms_probs = list(map(lambda fitness: fitness / total_fitness, chroms_fitness))

print(funcs.eval(chroms[1]), chroms_evals[1], total_fitness, chroms_probs[1])