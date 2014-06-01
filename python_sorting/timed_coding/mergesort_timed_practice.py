#!/usr/bin/env python3
# mergesort_timed_practice.py
# David Prager Branner
# 20140601, works, after 29 minutes.

def mergesort(lst):
    # Base case
    if len(lst) <= 1:
        return lst
    # Divide and conquer
    half = len(lst) // 2
    return recombine(mergesort(lst[:half]), mergesort(lst[half:]))

def recombine(list1, list2):
    combined = []
    counter1 = 0
    counter2 = 0
    while True:
        if list1[counter1] < list2[counter2]:
            combined.append(list1[counter1])
            counter1 += 1
            if counter1 == len(list1):
                combined.extend(list2[counter2:])
                break
        else:
            combined.append(list2[counter2])
            counter2 += 1
            if counter2 == len(list2):
                combined.extend(list1[counter1:])
                break
    return combined
