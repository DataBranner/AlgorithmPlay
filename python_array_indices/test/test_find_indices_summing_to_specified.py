# test_find_indices_summing_to_specified.py
# David Prager Branner
# 20131104

import pytest
import random
import sys
import os
sys.path.append(os.path.join('..'))
import find_indices_summing_to_specified as F

specified = 500
trials = 50
the_range = 2000

def test_all_sum_to_specified():
    for trial in range(trials):
        # generate random string
        array = [random.randint(1, (the_range * 10)) for i in range(the_range)]
        # get results
        pairs = F.main(specified, array)
        if not pairs:
            continue
        # See if each returned pair indeed adds up to "specified"
        assert [True for pair in pairs if sum(pair) - specified != 0] == []

def test_all_pairs_found():
    for trial in range(trials):
        # Prepare control list.
        # 1. Generate random integers less than half value of "specified".
        control_seeds = [random.randint(1, specified / 2 - 1)
                for i in range(the_range)]
        # 2. Eliminate duplicates, sort, and pair with expected matching values.
        control_seeds = list(set(control_seeds))
        control_seeds.sort()
        control_pairs = [(i, specified-i) for i in control_seeds]
        # 3. Construct array from the control pairs.
        array = control_seeds + [pair[1] for pair in control_pairs]
        # Output of F should match the control pairs.
        assert set(F.main(specified, array)) == set(control_pairs)

def test_no_pairs_found():
    for trial in range(trials):
        # Array contains only values less than half that of "specified", so no
        # matches are possible.
        array = [random.randint(1, specified / 2 - 1)
                for i in range(the_range)]
        assert F.main(specified, array) == None

