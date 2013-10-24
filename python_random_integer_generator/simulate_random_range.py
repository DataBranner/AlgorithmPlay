# simulate_random_range.py
# 20131021

'''Problem: If you have access to a function that returns a random integer from
one to "given", write another function which returns a random integer from one
to "desired".

Solution: Generate the sum of "desired" number of 1-to-"given" random numbers
and then find the modulus remainder; add 1 to make the range of results begin
at 1.

'''

import random

def main(given, desired):
    '''This version is slightly faster than the list-comprehension version.'''
    the_sum = 0
    for i in range(desired):
         the_sum += random.randint(1, given)
    return (the_sum % desired) + 1

def comprehension(given, desired):
    '''This version is slightly slower than main().'''
    the_sum = sum([random.randint(1, given) for i in range(desired)])
    return (the_sum % desired) + 1
