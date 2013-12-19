#! /usr/local/bin/python3
# permutation.py
# David Prager Branner
# 20131219
"""Given an input list, return a list of all permutations of it."""

def permutations_recursive(the_list):
    if len(the_list) == 1:
        return [the_list]
    to_return = []
    for i, item in enumerate(the_list):
        # Generate remainder: subset lacking index.
        remainder = tuple(the_list[:i] + the_list[i+1:])
        # Combine permutations of remainder with item.
        results = [(item,) + tuple(one_permutation)
                for one_permutation in permutations_recursive(remainder)]
        to_return.extend(results)
    return to_return

def permutations_dynamic(the_list, memoized={}):
    # Base case.
    if len(the_list) == 1:
        return [the_list]
    to_return = []
    for i, item in enumerate(the_list):
        # Generate remainder: subset lacking index.
        remainder = tuple(the_list[:i] + the_list[i+1:])
        # Memoize.
        if remainder not in memoized:
            memoized[remainder] = permutations_dynamic(remainder)
        # Combine permutations of remainder with item.
        results = [(item,) + tuple(one_permutation)
                for one_permutation in memoized[remainder]]
        to_return.extend(results)
    return to_return
