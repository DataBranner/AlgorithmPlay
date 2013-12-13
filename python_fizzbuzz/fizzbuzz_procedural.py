#!/usr/bin/env python3
# Filename: fizzbuzz_procedural.py
# Author: David Prager Branner
# Date: 20121205
"""Coding of fizzbuzz for Hacker School application. For Python v.2.7."""

import sys

def main():
    for i in range(1, 101):
        if i%3 and i%5:
            # neither of the special cases
            print(i)
        else:
            # the special cases
            if not i%3:
                # divisible by 3; we are not done yet so no linebreak
                print('Fizz', end='')
            if not i%5:
                # divisible by 5
                print('Buzz')
            else:
                # now add linebreak after Fizz case
                print('')

if __name__ == '__main__':
    main()
