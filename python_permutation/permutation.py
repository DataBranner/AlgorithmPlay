#! /usr/local/bin/python3
# permutation.py
# David Prager Branner
# 20131207
"""Given an input list, return a list of all permutations of it."""

def recursive(the_list):
    if len(the_list) == 1:
        return the_list
    to_return = []
    for i, item in enumerate(the_list):
        remainder = the_list[0:i] + (
                the_list[i+1:] if i < len(the_list) else None)
        # Use of isinstance needed to prevent tuple+non-tuple TypeError.
        results = [((item,) + (
                permuted if isinstance(permuted, tuple) else (permuted,))) 
                for permuted in recursive(remainder)]
        to_return.extend(results)
    return to_return
