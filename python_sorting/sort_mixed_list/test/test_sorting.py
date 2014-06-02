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

def test_sort_mixed_list_01():
    lst = [4, 'b', 3, 'g', 'a', 1, 2, 0.05]
    assert sort_mixed_list.main(lst) == [1, 'a', 2, 'b', 'g', 3, 4, 0.05]

def test_sort_mixed_list_02():
    lst = [2, 'a', 1, 'g', 3, 'c']
    assert sort_mixed_list.main(lst) == [1, 'a', 2, 'c', 3, 'g']

def test_insertionsort():
    lst = fill_random_list()
    lst2 = lst[:]
    assert sorted(lst) == sort_mixed_list.insertionsort(lst2)
