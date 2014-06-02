# test_sorting.py
# 20140602
# David Prager Branner

'''Test suite for Python implementation of some sorting algorithms.'''

import os
import sys
import random
sys.path.append(os.path.join('..'))
import sort_mixed_list

def fill_random_list(the_range=10000):
    return [random.randint(-100000, 100000) for i in range(the_range)]

def test_sort_mixed_list():
    lst = [4, 'b', 3, 'g', 'a', 1, 2, 0.05]
    sort_mixed_list.main(lst) == [1, 'a', 2, 'b', 'g', 3, 4, 0.05]
