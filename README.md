Genetic Algorithm
======

GA implementation for finding minimum of mathematical functions.

Files in `src` folder:
* models.py - data structures declarations
* constants.py - constants
* funcs.py - helper functions
* main.py - algorithm implementation

Current state handles at least two-variable functions. To increase the number of them, one should add another field to `Chromosome` class in `models.py` and adjust `eval` and `get_best_eval` functions in `funcs.py`

Stack
------

Name | Version
--- | ---
Python | 3.11.1
NumPy | 1.24.3
Matplotlib | 3.7.1
alive-progress | 3.1.2
