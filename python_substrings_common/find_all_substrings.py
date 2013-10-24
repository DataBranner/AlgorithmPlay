# find_all_substrings.py
# 20131022
# David Prager Branner

"""Generate all distinct non-empty substrings of a given string."""

import random
import string

def find_all_substrings(n=10):
    s = "".join([random.choice(string.ascii_lowercase) for i in range(n)])
    length = len(s)
    substrings = set()
    for start_index in range(length+1):
        # End of substring may always be as far away as at end of string.
        for end_index in range(start_index+1, length+1):
            substrings.add(s[start_index:end_index])
    return substrings
