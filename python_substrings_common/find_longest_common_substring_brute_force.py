# find_longest_common_substring_brute_force.py
# 20131023
# David Prager Branner

import random
import string

"""Find longest common non-empty substrings of input strings by brute force."""

def find_all_substrings(s, non_empty=True):
    """Generate all substrings of an input string."""
    length = len(s)
    substrings = set()
    for start_index in range(length+1):
        # End of substring may always be as far away as at end of string.
        for end_index in range(start_index+1, length+1):
            substrings.add(s[start_index:end_index])
    if not non_empty:
        substrings.add('')
    return substrings

def find_longest_common_substring(n=100, num_strings=2, strings=[], all=True):
    """Find the longest common non-empty substrings."""
    # Generate list of input strings if necessary.
    if strings:
        num_strings = len(strings)
    else:
        if num_strings < 2 or not isinstance(num_strings, int):
            num_strings = 2
        strings = ["".join([random.choice(string.ascii_lowercase) 
                for i in range(n)]) for j in range(num_strings)]
    #
    # Generate sets of substrings
    substrings_sets = []
    for item in strings:
        # Substring starts at each element of item in turn.
        substrings = find_all_substrings(item)
        substrings_sets.append(substrings)
    common_substrings = substrings_sets[0].intersection(*substrings_sets[1:])
    #
    # Find longest common substring.
    substrings_by_length = []
    longest = 0
    a_longest_substring = []
    for substring in common_substrings:
        length = len(substring)
        if length > longest:
            # We have new longest length; discard past matter and 
            #     re-initialize substrings_by_length.
            longest = length
            substrings_by_length = {(length, substring)}
        elif all and length == longest:
            # Substring matches earlier longest substrings in length.
            substrings_by_length.add((length, substring))
        # And if substring not longest, discard.
    return [length_and_substring[1] 
            for length_and_substring in substrings_by_length 
            if length_and_substring[0] == longest]
