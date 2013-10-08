# test_sorting.py
# 20130912
# David Prager Branner

'''Test suite for Python implementation of some sorting algorithms.'''

import os
import sys
import random
sys.path.append(os.path.join('..'))
import sorting

def fill_random_list(the_range=10000):
    return [random.randint(-100000, 100000) for i in range(the_range)]

def test_quicksort():
    the_list = fill_random_list()
    assert sorting.quicksort(the_list) == sorted(the_list)

def test_mergesort():
    the_list = fill_random_list()
    assert sorting.mergesort(the_list) == sorted(the_list)

def test_insertionsort():
    # Smaller range because slower sort.
    the_list = fill_random_list(1000)
    assert sorting.insertionsort(the_list) == sorted(the_list)

def test_zadrozny_insertionsort():
    the_list = fill_random_list(1000)
    assert sorting.zadrozny_insertionsort(the_list) == sorted(the_list)
