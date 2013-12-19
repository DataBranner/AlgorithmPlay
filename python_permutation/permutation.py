#! /usr/local/bin/python3
# permutation.py
# David Prager Branner
# 20131219
"""Given an input list, return a list of all permutations of it."""

def permutations_recursive(the_list):
    if len(the_list) == 1:
        return the_list
    to_return = []
    for i, item in enumerate(the_list):
        remainder = the_list[0:i] + (
                the_list[i+1:] if i < len(the_list) else None)
        # Use of isinstance needed to prevent tuple+non-tuple TypeError.
        results = [((item,) + (
                permuted if isinstance(permuted, tuple) else (permuted,))) 
                for permuted in permutations_recursive(remainder)]
        to_return.extend(results)
    return to_return

def permutations_dynamic(the_list, memoized={}):
    # Base case.
    if len(the_list) <= 1:
        return [the_list]
    to_return = []
    for i, item in enumerate(the_list):
        # Generate subset lacking index.
        subset = the_list[:i] + the_list[i+1:]
        # Memoization. Must convert to tuple for use as dictionary key.
        tuplized_subset = tuple(subset)
        if tuplized_subset in memoized:
            permutations_of_subset = memoized[tuplized_subset]
        else:
            permutations_of_subset = permutations_dynamic(subset)
            memoized[tuplized_subset] = permutations_of_subset
        # Combine permutations of subset with item.
        for element in permutations_of_subset:
            to_return.append((item,) + tuple(element))
    return to_return
