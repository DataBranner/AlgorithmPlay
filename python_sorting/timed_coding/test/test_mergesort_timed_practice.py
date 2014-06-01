# test_mergesort_timed_practice.py
# 20140601
# David Prager Branner

'''Test suite for Python implementation of some sorting algorithms.'''

import os
import sys
import random
sys.path.append(os.path.join('..'))
from mergesort_timed_practice import mergesort as M

def fill_random_list(the_range=10000):
    return [random.randint(-100000, 100000) for i in range(the_range)]

def test_mergesort_timed_practice():
    the_list = fill_random_list(1000)
    assert M(the_list) == sorted(the_list)
