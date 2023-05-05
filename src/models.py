from dataclasses import dataclass


@dataclass(frozen=True)
class Chromosome:
    x: float
    y: float
    # z: float