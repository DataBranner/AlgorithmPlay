# eratosthenes.py
# David Prager Branner
# 20131210, works
"""Implement the Sieve of Eratosthenes."""

import math
from collections import deque

def sift(number_of_primes):
    # 1. Figure size of initial sieve.
    # Can estimate nth prime <  n * log n * 1.25.
    if number_of_primes == 1:
        return [2]
    factor = 1.25
    upper_bound = (
            int(number_of_primes * math.log(number_of_primes) * factor)  + 1)
    # 2. Prepare array.
    sieve = deque([i for i in range(upper_bound+1)])
    sieve[0] = None
    sieve[1] = None
    # 3. Eliminate non-primes and reduce to array with no holes.
    primes = []
    counter = 0 # for advancing through sieve looking for survivors
    while len(primes) - number_of_primes < 0:
        # Find next survivor to add to primes.
        while not sieve[counter]:
            counter +=1
        new_prime = sieve[counter]
        primes.append(new_prime)
        # Do sifting — but only if new_prime is low enough.
        # Note that integers with more than one prime factor will be sifted
        # more than once, a failure of efficiency.
        if new_prime < math.sqrt(upper_bound):
            for index in range(new_prime*2, upper_bound+1, new_prime):
                sieve[index] = None
        counter += 1
    # Make sure number of primes is correct, in case of error.
    while len(primes) - number_of_primes > 0:
        primes.pop()
    return primes
