# powerset.py
# David Prager Branner
# 20131207
"""Return the power set of an input list."""

import itertools

def main(the_list):
    return [i for j in range(len(the_list)+1) for i in
            itertools.combinations(the_list, j)]
