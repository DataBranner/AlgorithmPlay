#!/usr/bin/env python3
# Filename: fizzbuzz_single_string.py
"""Variety of FizzBuzz seen in the wild.

Because it depends on string concatenation, slower than fizzbuzz_zip_cycles.py.
"""

for i in range(1, 101):
    print('Fizz' * (i%3 == 0) + 
            'Buzz' * (i%5 == 0) + 
            str(i) * ((i%5 != 0) and (i%3 !=0))
        )
