import pytest
import numpy
import random
import os
import sys
sys.path.append(os.path.join('..'))
import simulate_random_range

def test(trials=100000, given=5, desired=7):
    '''Compare the s.d. and mean of the output of a simulated random integer
    generator. The simulation assumes that you have a way of generating a
    random integer between 1 and "given", but instead need the range to be 1 to
    "desired".
    
    We measure the randomness of our result by keeping track of the output in
    an array, then taking the s.d. and mean of it. We compare the ratio of
    those to the ratio of the s.d. and mean of random.randint()'s output, and
    predict the two values will not differ by more than 2/3.'''
    # Set up our simulation.
    test_array = [0 for i in range(desired)]
    for i in range(trials):
        test_array[simulate_random_range.main(given, desired)-1] += 1
    test_ratio = numpy.std(test_array)/numpy.mean(test_array)
    # Set up control array.
    control_array = [0 for i in range(desired)]
    for i in range(trials):
        control_array[random.randint(1, desired)-1] += 1
    control_ratio = numpy.std(control_array)/numpy.mean(control_array)
    assert 1/3 < test_ratio/control_ratio < 3.0
