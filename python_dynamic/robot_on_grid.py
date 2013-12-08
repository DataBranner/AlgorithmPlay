# robot_on_grid.py
# David Prager Branner
# 20131208
"""From Laakman fifth ed. problem 9.2, first half.

Imagine a robot sitting on the upper-left corner of an X x Y grid. The robot
can only move in two directions: right and down. How many possible paths are
there for the robot to go from (0,0) to (X,Y)?
"""

import itertools
import math
import time
import sys

def main(X, Y):
    # The robot must travel X steps right and Y steps down in any case.
    # The only issue is the order. So we can enumerate the possible paths as
    # the permutation of an array of X right steps and Y down steps.
    path = ['r'] * X + ['d'] * Y
    #
    # 1. By calculation: C(Y+X, X)
    start_time = time.time()
    # But first we must ensure that Y is the larger of the two.
    X, Y = min(X, Y), max(X, Y)
    combinations = math.factorial(Y+X) // (
            math.factorial(X) * math.factorial(Y))
    print('Number of possible paths:\n    by calculation: {}; time: {:.6f}'.
            format(combinations, time.time() - start_time))
    #
    # 2. By enumeration; to check calculation. But very inefficient enumeration.
    print('    by enumeration: ', end='')
    sys.stdout.flush()
    start_time = time.time()
    all_paths = [item for item in itertools.permutations(path)]
    as_sets = len(set(all_paths))
    print('{}; time: {:.6f}'.
            format(as_sets, time.time() - start_time))
    #
    # 3. Report whether results are the same or not.
    print('\nThe two values are {}the same.'.format('' if as_sets ==
        combinations else 'not '))
