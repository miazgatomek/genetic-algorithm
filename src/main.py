import funcs
import common
from funcs import generate_chroms

chroms = generate_chroms(common.NUM_OF_CHROMS, common.NUM_GEN_RANGE)

print(chroms)