#!/usr/bin/env python3
# insertionsort_timed_practice.py
# David Prager Branner
# 20140601, works, after 8 minutes.

def insertionsort(lst):
    for i in range(len(lst)):
        while i > 0 and lst[i] < lst[i - 1]:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1
    return lst
